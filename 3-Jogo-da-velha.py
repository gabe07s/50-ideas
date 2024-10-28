def criar_tabuleiro():
    return [' '] * 9
def mostrar_tabuleiro(tabuleiro):
    print(f"""
     {tabuleiro[0]} | {tabuleiro[1]} | {tabuleiro[2]}
    ---+---+---
     {tabuleiro[3]} | {tabuleiro[4]} | {tabuleiro[5]}
    ---+---+---
     {tabuleiro[6]} | {tabuleiro[7]} | {tabuleiro[8]}
    """)

def verificar_vitoria(tabuleiro, jogador):
    combinacoes_vencedoras = [
        [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Linhas
        [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Colunas
        [0, 4, 8], [2, 4, 6]              # Diagonais
    ]
    return any(all(tabuleiro[i] == jogador for i in comb) for comb in combinacoes_vencedoras)

def verificar_empate(tabuleiro):
    return ' ' not in tabuleiro

def jogar():
    """Executa o jogo da velha."""
    tabuleiro = criar_tabuleiro()
    jogador_atual = 'X'

    print("Bem-vindo ao Jogo da Velha!")
    mostrar_tabuleiro(tabuleiro)

    while True:
        try:
            posicao = int(input(f"Jogador {jogador_atual}, escolha uma posição (1-9): ")) - 1
            if tabuleiro[posicao] != ' ':
                print("Essa posição já está ocupada. Escolha outra!")
                continue
        except (ValueError, IndexError):
            print("Entrada inválida! Digite um número entre 1 e 9.")
            continue

        # Faz a jogada
        tabuleiro[posicao] = jogador_atual
        mostrar_tabuleiro(tabuleiro)

        # Verifica vitória
        if verificar_vitoria(tabuleiro, jogador_atual):
            print(f"Parabéns! Jogador {jogador_atual} venceu!")
            break

        # Verifica empate
        if verificar_empate(tabuleiro):
            print("Empate! Ninguém venceu.")
            break

        # Troca o jogador
        jogador_atual = 'O' if jogador_atual == 'X' else 'X'

if __name__ == "__main__":
    jogar()
