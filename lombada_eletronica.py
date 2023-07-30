velocidade_km = int(input('Digite a velocidade KM/H '))
if velocidade_km <= 80:
    print('Você está na velocidade permitida!')


else:
    velocidade_km > 80
    multa = (velocidade_km - 80) * 7
    print('Você foi multado! O valor da sua multa é de:',multa,'R$')
