#Crie um algoritimo que leia um número e mostre o seu dobro, triplo e raiz quadrada.
n = int(input('Escreva um número: '))
dobro = n * 2
triplo = n * 3
raiz = int(n ** (1/2))

print(f'O dobro de {n} é {dobro} o triplo é {triplo} e a raiz é {raiz}')