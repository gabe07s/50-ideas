import os
import random
os.system ('clear || cls')

contador = 0
numero = random.randint(1, 1000)
while True:
    num_escolhido = int(input ("Escolha o número de 1 á 1000: "))
    if num_escolhido == numero:
        print ("PARABÉNS!! NÚMERO CORRETO!!\n")
        contador += 1
        break
    elif num_escolhido > numero:
        print("Número escolhido maior, diminua\n")
        contador += 1
    elif num_escolhido < numero:
        print("Número escolhido menor, aumente\n")
        contador += 1

print(f"Foram {contador} tentativas")

