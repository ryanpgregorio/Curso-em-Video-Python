#Escreva um programa que leia um valor em metros e o exiba convertido em centimetro e milimetros.
m = float(input('Digite quantos metros tem sua rua: '))
cm = m * 10 * 10
mm = cm * 10

print(f'Sua rua tem {m}m, {cm}cm e {mm}mm!')