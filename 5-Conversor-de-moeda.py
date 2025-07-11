import os
os.system ('clear || cls')

moeda = input("Moedas disponiveis: Dólar, Euro, Libra, Iene, Franco, Yuan, Peso, Lira. \nEscolha qual moeda você gostaria de converter do real? ")
real = float(input(f"Quanto do real você gostaria de passar para {moeda}? "))

match moeda:
    case "Dólar":
        resultado = real * 0.18
    case "Euro":
        resultado = real * 0.16
    case "Libra":
        resultado = real * 0.13
    case "Iene": 
        resultado = real * 26.51    
    case "Franco":
        resultado = real * 0.14
    case "Yuan":
        resultado = real * 1.26
    case "Peso":
        resultado = real * 226.63
    case "Lira": 
        resultado = real * 7.22
    
print(f"O total em {moeda} é: {resultado}.")