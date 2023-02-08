#Faça um programa que leia uma frase pelo teclado e mostre quantas vezes aparece a letra “A”, em que posição ela aparece 
#a primeira vez e em que posição ela aparece a última vez.
frase = str(input('Digite qualquer frase: ')).lower().strip()

print(f'A letra "A" aparece {frase.count("a")} vezes!\nA letra "A" aparece pela primera vez na {frase.find("a")+1}° casa!\nAparece pela ultima vez na {frase.rfind("a")+1}° casa!')