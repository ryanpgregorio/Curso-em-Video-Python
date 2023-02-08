#Faça um programa que leia o nome completo de uma pessoa, mostrando em seguida o primeiro e o último nome separadamente.
name = str(input('Digite seu nome completo: ')).lower().strip()
firt = name.split()
last = name.rfind(' ')
print(f'Muito Prazer!!!\nSeu primeiro nome é {firt[0]}\nSeu último nome é {name[last:]}')

