#Faça um programa que leia a largura e a altura de uma parede em metros, calcule a sua área e a quantidade de tinta 
# necessária para pintá-la, sabendo que cada litro de tinta, pinta uma área de 2m²
print(f'{"="*15}cálculo para pintura{"="*15}')

l = float(input('Digite a largura da parede: '))
a = float(input('Digite a altura da parede: '))

area = l * a
tinta = area / 2

print(f'Serão necessários {tinta}L de tinta para pintar sua parede!')