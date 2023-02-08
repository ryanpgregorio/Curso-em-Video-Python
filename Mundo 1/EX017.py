#Faça um programa que leia compriumento do cateto oposto e do cateto adjacente de um triângulo retangulo, calcule e 
#mostre o comprimento da hipotenusa.
import math
co = float(input('Digite o comprimento do cateto oposto: '))
ca = float(input('Digite o comprimento do cateto adjacente: '))

h = math.hypot(co, ca)

print(f'A hipotunesa ira medir {h:.2f}')