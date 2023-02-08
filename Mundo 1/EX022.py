#Crie um programa que leia o nome completo de uma pessoa e mostre:
#O nome com todas as letras maiúsculas e minúsculas.
#Quantas letras ao todo (sem considerar espaços).
#Quantas letras tem o primeiro nome.
name = str(input('Digite seu nome completo: ')).strip()
separa = name.split()

print(f'Seu nome com todas as letras maiúsculas fica {name.upper()}')
print(f'Seu nome com todas as letras maiúsculas fica {name.lower()}')
print(f'Seu nome possui {len(name) - name.count(" ")} letras!')
print(f'Seu primero nome é {separa[0]} e tem {len(separa[0])} letras!')