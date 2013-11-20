v_mer = float(input("Entre com valor da mercadoria: "))
v_per = float(input("Entre com a porcentagem do desconto: "))
v_desconto = v_mer * (v_per/100)
v_prefinal = v_mer - v_desconto
print ("O valor de desconto: R$%.2f" % v_desconto)
print ("O valor a pagar: R$%.2f" % v_prefinal)