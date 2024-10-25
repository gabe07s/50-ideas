import os
os.system("clear||cls")

historico = []
resultado = 0.0
contador = 0
while True:
    contador += 1 
    if contador == 2:
        print (f"O resultado anterior {resultado}")
    entrada = input(f"Digite a nota(Ou se preferir finalizar, escreva 'sair' ): ")

    if entrada.lower() == 'sair':
        print("Encerrando a calculadora.")
        break

    try:
        num1 = float(entrada)
    except ValueError:
        print("Entrada inválida! Por favor, digite um número válido.")
        continue
    
    operador = input("Digite o operador (+, -, *, /): ")
    
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
        case _:
            print("Utilize um operador verdadeiro.")
    historico.append(operacao)
    print("\nHistórico de operações:")
    for op in historico:
        print(op)
    print("\n" + "=" * 30 + "\n")
