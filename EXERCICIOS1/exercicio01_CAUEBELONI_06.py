distancia = float(input("Qual a distancia a percorrer em quilometros: "))
velocidade = float(input("Qual a velocidade media em km/h: "))
         
tempo = (distancia / velocidade) * 60
horas = int(tempo / 60)
minutos = int(tempo % 60)
print 'O tempo para completar a viagem e de %d hora(s) e %d minutos(s)' % (horas,minutos)