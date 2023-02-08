#Faça um programa que leia um ângulo qualquer e mostre na tela o valor do seno, cosseno e tangente desse ângulo.
import math
a = int(input('Digite um ângulo: '))

c = math.cos(math.radians(a))
s = math.sin(math.radians(a))
t = math.tan(math.radians(a))


print(f'O seno de {a}° é {s:.2f} \nO cosseno de {a}° é {c:.2f} \nA tangente de {a}° é {t:.2f}')