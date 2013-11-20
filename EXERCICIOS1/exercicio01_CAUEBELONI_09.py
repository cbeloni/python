quilometros = input("Quantos quilometros foram percorridos? ")         
dias = input("Por quantos dias o carro foi alugado? ")         
conta = float(quilometros*0.15) + float(dias*60)
print 'O valor da conta é: R$ %.2f ' % (conta)