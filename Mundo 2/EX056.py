#Desenvolva um programa que leia o nome, idade e sexo de 4 pessoas.
#No final do programa, mostre: a média de idade do grupo, qual é o nome do homem mais velho e quantas mulheres têm menos de 20 anos.
soma_idade = 0
media_idade = 0
maior_idade_homem = 0
nome_velho = 0
totmulher20 = 0

for p in range (1, 5):
    print(f'-----{p}° PESSOA-----')
    nome = str(input('Nome: '))
    idade = int(input('Idade: '))
    sexo = str(input('Sexo [M/F]: ')).strip()
    soma_idade += idade
    
    if p == 1 and sexo in 'Mm':
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Mm' and idade > maior_idade_homem:
        maior_idade_homem = idade
        nome_velho = nome
    if sexo in 'Ff' and idade < 20:
        totmulher20 += 1

mediaidade = soma_idade / 4
print(f'A média de idade do grupo é de {mediaidade} anos!')
print(f'O homem mais velho tem {maior_idade_homem} anos e se chama {nome_velho}!')
print(f'Ao todo são {totmulher20} mulher com menos de 20 anos!')