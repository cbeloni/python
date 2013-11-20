v_dias = int(input("Entre com a quantidade de dias: "))
v_hora = int(input("Entre com a quantidade de horas: ")) 
v_min = int(input("Entre com a quantidade de minutos : ")) 
v_seg = int(input("Entre com a quantidade de segundos: "))

v_hora = (v_dias*24) + v_hora
v_min  = (v_hora*60) + v_min
v_seg  = (v_min*60) + v_seg

print ("A quantidade de segundos e: %d" % v_seg) 