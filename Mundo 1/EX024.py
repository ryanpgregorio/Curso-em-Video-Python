#Crie um programa que leia o nome de uma cidade diga se ela começa ou não com o nome “SANTO”.
city = str(input('Digite o nome da sua cidade: ')).lower().lstrip()
separa = city.split()

if separa[0] == 'santo':
    print(f'{city} começa com santo!')

else:
    print(f'{city} não começa com santo!')


"""if cc < "santo":
    print(f'{city} não começa com santo!')

elif cc > "santo":
    print(f'{city} começa com santo!')

else:
    (f'{city} não tem santo')"""