#Desenvolva uma lógica que leia o peso e a altura de uma pessoa, calcule seu Índice de Massa Corporal (IMC) 
# e mostre seu status, de acordo com a tabela abaixo:
#IMC abaixo de 18,5: Abaixo do Peso
#Entre 18,5 e 25: Peso Ideal
#25 até 30: Sobrepeso
#30 até 40: Obesidade
#Acima de 40: Obesidade Mórbida
peso = float(input('Digite seu peso: '))
altura = float(input('Digite sua altura: '))

imc = peso / (altura * altura)

print(' ')

if imc <= 18.5:
    print(f'Seu IMC é {imc}, você está abaixo do peso! PROCURE COMER MAIS CARBOIDRATOS')

elif imc >= 18.5 and imc < 25:
    print(f'Seu IMC é {imc:.1f}, você está no peso ideal!')

elif imc >= 25 and imc < 30:
    print(f'Seu IMC é {imc:.1f}, você está sobrepeso! CUIDADO!')

elif imc >= 30 and imc < 40:
    print(f'Seu IMC é {imc:.1f}, você está com obesidade! FAÇA EXERCICIOS E DIETA!')

elif imc >= 40:
    print(f'Seu IMC é {imc:.1f}, você está com obesidade mórbida! PROCURE UM MÉDICO IMEDIATAMENTE!')



