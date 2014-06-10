spool c:\sati\log_Chamado_6223905.txt 
 
PROMPT --**************************** [ INICIO DA APLICA�AO ] ***********************************--;
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
SET SERVEROUTPUT OFF 
set linesize 1000 
set pagesize 4000 
set define off 
PROMPT --**************************** [ ALTER SESSION PARA NLS_DATE_FORMAT = 'DD/MM/YYYY' ] *****--;
alter session set nls_date_format = 'dd/mm/yyyy'; 
PROMPT --**************************** [ APLICANDO 'CRIANDO TABELA DE LOG DE MENSAGENS' ] *****--;
@c:\sati\LF_TAB_LOG_PACOTE_CREATE.SQL 
PROMPT --**************************** [ APLICANDO 01_P_CTM_ALT_PERM_6223905_221113_1000.SQL ] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@c:\sati\01_P_CTM_ALT_PERM_6223905_221113_1000.SQL 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
 
PROMPT --**************************** [ APLICANDO 02_PWF_MENU_INSERT_6223905_221113_1000.sql ] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@c:\sati\02_PWF_MENU_INSERT_6223905_221113_1000.sql 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
 
PROMPT --**************************** [ APLICANDO 02_P_CTM_RELAT_ALT_6223905_221113_1000.SQL ] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@c:\sati\02_P_CTM_RELAT_ALT_6223905_221113_1000.SQL 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
 
PROMPT --**************************** [ APLICANDO 03_P_CTM_ALTERARLOTE_6223905_221113_1000.SQL ] *********************--; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') INICIO_APLICACAO FROM DUAL; 
@c:\sati\03_P_CTM_ALTERARLOTE_6223905_221113_1000.SQL 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
 
PROMPT --**************************** [ LOG DE MENSAGENS ] ******************************--;
SELECT * FROM LF_TAB_LOG_PACOTE WHERE CHAMADO = '6223905'; 
PROMPT --**************************** [ APLICANDO 'COMPILA2.SQL' ] ******************************--;
@c:\sati\compila2.sql 
PROMPT --**************************** [ APLICANDO 'ALL_ERRORS.SQL' ] ****************************--;
@c:\sati\all_errors.sql 
PROMPT --**************************** [ DADOS DA APLICACAO ] *************************************--;
show user; 
SELECT COD_HOLDING FROM LF_EMPRESA_HOLDING; 
show parameters db_name; 
SELECT GLOBAL_NAME FROM GLOBAL_NAME; 
SELECT INSTANCE_NAME, VERSION FROM V$INSTANCE; 
SELECT TO_CHAR(SYSDATE,'dd/mm/yyyy hh24:mi:ss') FIM_APLICACAO FROM DUAL; 
PROMPT --**************************** [ FIM DA APLICA�AO ] **************************************--;
 
spool off 
