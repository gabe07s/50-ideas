import os
os.system ('clear || cls')

numero_um = int(input("Qual o primeiro número? "))
operador = input("Qual operação irá usar? (Use os seguintes sinais '+, -, *, /') ")
numero_dois = int(input("Qual o segundo número? "))

match operador:
    case '+':
        resultado = numero_um + numero_dois
        print(f"{numero_um} + {numero_dois} = {resultado}")
    case '-':
        resultado = numero_um - numero_dois
        print(f"{numero_um} - {numero_dois} = {resultado}")
    case '*':
        resultado = numero_um * numero_dois
        print(f"{numero_um} * {numero_dois} = {resultado}")
    case '/':
        if numero_dois != 0:
            resultado = numero_um / numero_dois
            print(f"{numero_um} / {numero_dois} = {resultado}")
        else:
            print("Não é possivel dividir por zero.")
    case _:
        print("Utilize um operador verdadeiro.")
        