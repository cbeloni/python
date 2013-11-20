v_sal = float(input("Entre com o salario: "))
v_per = float(input("Entre com a porcentagem do aumento: "))
v_aumento = v_sal * (v_per/100)
v_salfinal = v_sal + v_aumento
print ("O valor de aumento: R$%.2f" % v_aumento)
print ("O valor do novo salario: R$%.2f" % v_salfinal)