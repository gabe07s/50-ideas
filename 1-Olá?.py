import os
os.system ('clear || cls')

print ("Olá meu amigo, um segundo, como você chegou aqui??? Na verdade, isso não importa, olá?")
while True:
    comprimento = input("Resposta: ")
    if comprimento.lower() == 'olá' or 'ola' or 'oi' or 'opa' or 'iae':
        print(" :)")
        break
    else:
        print("AVISO: Responda ele, seja uma pessoa normal!")