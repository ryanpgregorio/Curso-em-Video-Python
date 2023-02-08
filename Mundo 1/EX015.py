#Escreva um programa que pergunte a quantidade de Km percorridos por um carro alugado e a quantidade de dias 
#pelos quais ele foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$60 por dia e R$0,15 por Km rodado.
dias = int(input('Digite quantos dias alugados: '))
km = float(input('Digite quantos kilometros percorreu: '))

sd = 60 * dias
skm = 0.15 * km
st= sd + skm

print(f'O total a pagar é R${st}')