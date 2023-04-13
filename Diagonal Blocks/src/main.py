''''
from games.connect4.players.greedy import GreedyConnect4Player
from games.connect4.players.minimax import MinimaxConnect4Player
from games.connect4.players.random import RandomConnect4Player
from games.connect4.simulator import Connect4Simulator
from games.game_simulator import GameSimulator
'''

''''
def run_simulation(desc: str, simulator: GameSimulator, iterations: int):
    print(f"----- {desc} -----")

    for i in range(0, iterations):
        simulator.change_player_positions()
        simulator.run_simulation()

    print("Results for the game:")
    simulator.print_stats()


def main():
    print("ESTG IA Games Simulator")

    num_iterations = 1000

    c4_simulations = [
        # uncomment to play as human
        #{
        #    "name": "Connect4 - Human VS Random",
        #    "player1": HumanConnect4Player("Human"),
        #    "player2": RandomConnect4Player("Random")
        #},
        {
            "name": "TicTacToe - Random VS Random",
            "player1": RandomConnect4Player("Random 1"),
            "player2": RandomConnect4Player("Random 2")
        },
        {
            "name": "TicTacToe - Greedy VS Random",
            "player1": GreedyConnect4Player("Greedy"),
            "player2": RandomConnect4Player("Random")
        },
        {
            "name": "Minimax VS Random",
            "player1": MinimaxConnect4Player("Minimax"),
            "player2": RandomConnect4Player("Random")
        },
        {
            "name": "Minimax VS Greedy",
            "player1": MinimaxConnect4Player("Minimax"),
            "player2": GreedyConnect4Player("Greedy")
        }
    ]


    for sim in c4_simulations:
        run_simulation(sim["name"], Connect4Simulator(sim["player1"], sim["player2"]), num_iterations)


'''

''''''
# Definir as dimensões do tabuleiro e das células
import pygame
LARGURA_TELA = 400
ALTURA_TELA = 400
TAMANHO_CELULA = 20
NUM_CELULAS = 20

peca = [[False, True, False, False, False],
        [True, True, True, False, False],
        [False, False, False, False, False],
        [True, True, True, False, False],
        [True, True, True, False, False]]


def desenhar_peca(screen, peca, posicao, cor):
    for y, linha in enumerate(peca):
        for x, ocupada in enumerate(linha):
            if ocupada:
                pygame.draw.rect(screen, cor, pygame.Rect(
                    (posicao[0] + x) * TAMANHO_CELULA, (posicao[1] + y) * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA))


def pode_colocar_peca(tabuleiro, peca, posicao):
    for y, linha in enumerate(peca):
        for x, ocupada in enumerate(linha):
            if ocupada and tabuleiro[posicao[1] + y][posicao[0] + x]:
                return False
    return True


def colocar_peca(tabuleiro, peca, posicao):
    for y, linha in enumerate(peca):
        for x, ocupada in enumerate(linha):
            if ocupada:
                tabuleiro[posicao[1] + y][posicao[0] + x] = True


def desenhar_tabuleiro(screen):
    for x in range(NUM_CELULAS):
        for y in range(NUM_CELULAS):
            cor = (255, 255, 255)  # cor branca para células vazias
            pygame.draw.rect(screen, cor, pygame.Rect(
                x * TAMANHO_CELULA, y * TAMANHO_CELULA, TAMANHO_CELULA, TAMANHO_CELULA), 1)


def dentro_do_tabuleiro(posicao, NUM_CELULAS, TAMANHO_CELULA):
    """
    Verifica se a posição da célula superior esquerda da peça está dentro do tabuleiro.
    posicao: tupla (x,y) com as coordenadas da célula superior esquerda da peça.
    tam_tabuleiro: inteiro com o tamanho do tabuleiro (largura e altura iguais).
    tam_peca: inteiro com o tamanho da peça (largura e altura iguais).
    Retorna True se a posição está dentro do tabuleiro e False caso contrário.
    """
    x, y = posicao
    if x < 0 or y < 0:
        return False
    if x + TAMANHO_CELULA > NUM_CELULAS or y + TAMANHO_CELULA > NUM_CELULAS:
        return False
    return True


def main():
    pygame.init()

    # Criar a janela do jogo
    screen = pygame.display.set_mode((LARGURA_TELA, ALTURA_TELA))
    pygame.display.set_caption('Diagonal Blocks')

    # Desenhar o tabuleiro
    desenhar_tabuleiro(screen)

    ''''
    while True:
        posicao_str = input("Digite a posição (x,y) da célula superior esquerda da peça: ")
        posicao = tuple(map(int, posicao_str.split(',')))
        if pode_colocar_peca(screen, peca, posicao) and dentro_do_tabuleiro(posicao, TAMANHO_CELULA, TAMANHO_CELULA):
            break
        else:
            print("Posição inválida. Tente novamente.")
    '''
    # Loop principal do jogo

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                return
            elif event.type == pygame.MOUSEBUTTONDOWN:
                # Obter as coordenadas do mouse
                pos = pygame.mouse.get_pos()

                # Converter as coordenadas do mouse para coordenadas de célula
                x = pos[0] // TAMANHO_CELULA
                y = pos[1] // TAMANHO_CELULA

                # Imprimir as coordenadas da célula clicada
                print(f"Célula selecionada: ({x}, {y})")

        pygame.display.flip()


if __name__ == '__main__':
    main()

'''
peça L: { [ (i,j), (i,j+1), (i,j+2), (i-1, j+2)]
        
}

'''
