#Desenvolva um programa que leia as três notas de um aluno, calcule e mostre a sua média.
name = str(input('Digite o nome do aluno: '))
n1 = float(input('Digite a primeira nota: '))
n2 = float(input('Digite a segunda nota: '))
n3 = float(input('Digite a terceira nota: '))
soma = (n1 + n2 + n3) / 3 

print(f'A média do {name} é {soma}')