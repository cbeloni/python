CREATE OR REPLACE PROCEDURE 
P_CTM_ALTERARLOTE (P_HOLDING      IN LF_NF_ENTRADA.COD_HOLDING %TYPE,
				   P_MATRIZ       IN LF_NF_ENTRADA.COD_MATRIZ %TYPE,
				   P_FILIAL       IN LF_NF_ENTRADA.COD_FILIAL %TYPE,
				   P_DATAINI      IN VARCHAR2,
				   P_DATAFIM      IN VARCHAR2,
				   P_CFOP 		  IN VARCHAR2,
				   P_TPLANC       IN VARCHAR2,
				   P_USUARIO      IN VARCHAR2,
				   P_EXIST        IN OUT INTEGER) IS 

V_TABELA NUMBER(2);
V_CFOP   VARCHAR2(4);

CURSOR CNFE (V_FILIAL VARCHAR2) IS

   SELECT  B.COD_HOLDING, 
   		   B.COD_MATRIZ, 
   		   B.COD_FILIAL, 
   		   B.ID_NF_ENTRADA, 
   		   A.ID_ITEM, 
   		   A.COD_IMPOSTO, 
   		   A.COD_TP_LANC_IMP,
   		   B.DT_ENTRADA,
   		   B.NUM_NF,
   		   B.SERIE,
   		   B.DOCNUM,
   		   B.COD_CFOP_LEGAL
      FROM LF.LF_NF_ENTRADA_IMPOSTO A, 
   	       LF.LF_NF_ENTRADA B, 
    	   LF.LF_NF_ENTRADA_ITEM C
     WHERE UPPER(A.COD_HOLDING)	= UPPER(P_HOLDING)
	   AND UPPER(A.COD_MATRIZ) 	= UPPER(P_MATRIZ)
	   AND UPPER(A.COD_FILIAL)	= UPPER(V_FILIAL)
	   AND A.COD_TP_LANC_IMP 	= '1'
	   AND B.COD_CFOP_LEGAL 	in (SELECT COD_CFOP_LEGAL FROM  LF.LF_TEMP_CFOPS)
	   AND DT_ENTRADA BETWEEN TO_DATE(P_DATAINI,'DD/MM/YYYY') 
	   					  AND TO_DATE(P_DATAFIM,'DD/MM/YYYY')
	   AND A.COD_IMPOSTO 		= '01'
	   AND B.COD_STATUS 		= '01'					  

	   --AND B.ID_NF_ENTRADA 		= 'I0005087'

	   AND B.COD_HOLDING   		= C.COD_HOLDING
	   AND B.COD_MATRIZ    		= C.COD_MATRIZ
	   AND B.COD_FILIAL    		= C.COD_FILIAL
	   AND B.ID_NF_ENTRADA 		= C.ID_NF_ENTRADA

	   AND C.COD_HOLDING 		= A.COD_HOLDING
	   AND C.COD_MATRIZ 		= A.COD_MATRIZ
	   AND C.COD_FILIAL 		= A.COD_FILIAL
	   AND C.ID_NF_ENTRADA	 	= A.ID_NF_ENTRADA
	   AND C.ID_ITEM 			= A.ID_ITEM;
   
vNFE   CNFE    %ROWTYPE;

CURSOR   CUSUARIO IS
    SELECT   USF.COD_MATRIZ,
             USF.COD_FILIAL,
             USF.COD_HOLDING,
             USF.COD_USUARIO,
             FIL.RAZAOSOCIAL,
             FIL.COD_UF
        FROM LF_USUARIO_FILIAL USF,
             LF_EMPRESA_FILIAL FIL
       WHERE USF.COD_HOLDING    = P_HOLDING
         AND UPPER(USF.COD_MATRIZ)     = UPPER(P_MATRIZ)
         AND UPPER(USF.COD_FILIAL)     LIKE UPPER(P_FILIAL)
         AND UPPER(USF.COD_USUARIO)    = UPPER(P_USUARIO)
         AND USF.COD_HOLDING    = FIL.COD_HOLDING
         AND USF.COD_MATRIZ     = FIL.COD_MATRIZ
         AND USF.COD_FILIAL     = FIL.COD_FILIAL
    ORDER BY USF.COD_HOLDING,
             USF.COD_MATRIZ,
             USF.COD_FILIAL,
             USF.COD_USUARIO;
VUSUARIO  CUSUARIO  %ROWTYPE;

PROCEDURE CRIAR_TABELA_LOG IS
BEGIN
	EXECUTE IMMEDIATE 'CREATE TABLE T_LOG_ALTERARLOTE (COD_MATRIZ VARCHAR2(50),COD_FILIAL VARCHAR2(50),PERIODO DATE, USUARIO VARCHAR2(50),DATATUAL DATE, NUM_NF VARCHAR(10),SERIE VARCHAR(10),DT_ENTRADA DATE,DOCNUM VARCHAR(10),CFOP VARCHAR2(4))';
	--DBMS_OUTPUT.PUT_LINE('CRIOU TABELA LOG');
END;

PROCEDURE CRIAR_TABELA_CFOPS IS
BEGIN
	EXECUTE IMMEDIATE 'CREATE GLOBAL TEMPORARY TABLE LF_TEMP_CFOPS(COD_CFOP_LEGAL VARCHAR(4))';
	--DBMS_OUTPUT.PUT_LINE('CRIOU TABELA CFOPS');
END;

PROCEDURE INSERE_CFOPS(V_CFOPS VARCHAR2) IS
V_QTD  NUMBER;
V_CFOP VARCHAR2(4);
BEGIN
V_QTD := LENGTH(V_CFOPS);
FOR i IN 1..V_QTD LOOP     
     IF (SUBSTR(V_CFOPS,i,1) = ';') THEN
     	INSERT INTO LF_TEMP_CFOPS VALUES (LPAD(V_CFOP,4,'0'));
     	V_CFOP := '';
     ELSE
     	V_CFOP := V_CFOP || SUBSTR(V_CFOPS,i,1);
     END IF;
END LOOP;
END;

BEGIN
	P_EXIST := 0;
	--RAISE_APPLICATION_ERROR(-20001,'HOLDING: '||P_HOLDING||' MATRIZ: '||P_MATRIZ||' FILIAL: '||P_FILIAL||' INI: '||P_DATAINI||' FIM: '||P_DATAFIM||'P_TPLANC'||P_TPLANC);
	--RAISE_APPLICATION_ERROR(-20001,'USUARIO: '||P_USUARIO);
	
	--DBMS_OUTPUT.PUT_LINE('VERIFICA SE TABELAS DE LOG E CFOPS EXISTEM');
	SELECT COUNT(1) 
	INTO V_TABELA
	FROM USER_TABLES 
	WHERE TABLE_NAME = 'T_LOG_ALTERARLOTE';
	
	IF (V_TABELA = 0) THEN
		CRIAR_TABELA_LOG;
	END IF;

	SELECT COUNT(1) 
	INTO V_TABELA
	FROM USER_TABLES 
	WHERE TABLE_NAME = 'LF_TEMP_CFOPS';
	
	IF (V_TABELA = 0) THEN
		CRIAR_TABELA_CFOPS;
	END IF;

	--DBMS_OUTPUT.PUT_LINE('INSERE CFOPS EM TEMPORARY TABLE');
	INSERE_CFOPS(P_CFOP);


    FOR VUSUARIO IN CUSUARIO 
    LOOP

		OPEN CNFE (VUSUARIO.COD_FILIAL);
		FETCH CNFE INTO vNFE;
    	
	  	WHILE CNFE%FOUND 
	  	LOOP
						 
			BEGIN        
	            UPDATE LF.LF_NF_ENTRADA_IMPOSTO 
	               SET COD_TP_LANC_IMP  = P_TPLANC
			     WHERE COD_HOLDING 		= vNFE.COD_HOLDING
			       AND COD_MATRIZ 		= vNFE.COD_MATRIZ
			       AND COD_FILIAL 		= vNFE.COD_FILIAL
			       AND ID_NF_ENTRADA 	= vNFE.ID_NF_ENTRADA
			       AND ID_ITEM 			= vNFE.ID_ITEM
			       AND COD_IMPOSTO 		= vNFE.COD_IMPOSTO
			       AND COD_TP_LANC_IMP  = vNFE.COD_TP_LANC_IMP;

			       INSERT INTO T_LOG_ALTERARLOTE (COD_MATRIZ,COD_FILIAL,PERIODO, USUARIO,DATATUAL,NUM_NF,SERIE,DT_ENTRADA,DOCNUM,CFOP)
			        VALUES (vNFE.COD_MATRIZ, vNFE.COD_FILIAL, P_DATAINI,P_USUARIO,sysdate,vNFE.NUM_NF,vNFe.SERIE,vNFE.DT_ENTRADA,vNFE.DOCNUM,vNFE.COD_CFOP_LEGAL);

			        P_EXIST := 1;
		    EXCEPTION WHEN OTHERS THEN
		    	NULL;
		    END;   

			 
		FETCH CNFE INTO vNFE;
		END LOOP;

		CLOSE CNFE;	

	END LOOP;	

	
	--PKG_Relatorio.GrvLinha('');
	IF (P_EXIST = 1) THEN
		P_CTM_RELAT_ALTERARLOTE(P_HOLDING,P_MATRIZ,P_FILIAL,P_DATAINI,P_DATAFIM,P_USUARIO,P_EXIST);
		COMMIT;
	ELSE
		ROLLBACK; 
	END IF; 	
END;
/
GRANT EXECUTE ON  P_CTM_ALTERARLOTE TO USER_LF
/