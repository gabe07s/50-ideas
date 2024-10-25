import os
os.system("clear||cls")

historico = []
resultado = 0.0
contador = 0
while True:
    contador += 1 
    if contador >= 2:
        print (f"O resultado anterior {resultado}")
        entrada = input("Deseja sair? Se sim, escreva 'sair'. Se quiser continuar, aperte 'enter'. ")
    else:
        entrada = input("Digite a nota(Ou se preferir finalizar, escreva 'sair' ): ")

    if entrada.lower() == 'sair':
        print("Encerrando a calculadora.")
        break

    try:
        if contador >= 2:
            num1 = resultado
        else:
            num1 = float(entrada)
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")
        continue
    
    while True:
        operador = input("Digite o operador (+, -, *, /): ")
        if operador != '+' or '-' or '*' or '/':
            print("3")
            print("Utilize um operador verdadeiro. +|-|*|/")
        else: 
            print("4")
            break
    
    try:
        num2 = float(input(f"Digite a nota: "))
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")
        continue
    match operador:
        case '+':
            resultado = num1 + num2
            operacao = (f"{num1} + {num2} = {resultado}")
        case '-':
            resultado = num1 - num2
            operacao = (f"{num1} - {num2} = {resultado}")
        case '*':
            resultado = num1 * num2
            operacao = (f"{num1} * {num2} = {resultado}")
        case '/':
            if num2 != 0:
                resultado = num1 / num2
                operacao = (f"{num1} / {num2} = {resultado}")
            else:
                print("Não é possivel dividir por zero.")
    historico.append(operacao)
    print("\nHistórico de operações:")
    for op in historico:
        print(op)
    print("\n" + "=" * 30 + "\n")
