import pygame
from cores import *
from randomizar import *
import sys
from time import sleep
from funcoes_tela import *

pygame.init()

# Configurações do display
pygame.display.set_caption('Treasure Hunt')                  # Nome do jogo na janela
icone = pygame.image.load('assets/imagens/tesouro.png')      # Personalização do ícone
pygame.display.set_icon(icone)

# Fontes
fonte = pygame.font.SysFont("Comic Sams MS", 50)
pirata_fonte = pygame.font.Font("assets/fonte/Caribbean.ttf", 30)
pirata_fonte_f = pygame.font.Font("assets/fonte/Caribbean.ttf", 50)

# Configurações de musica
pygame.mixer.music.load('assets/musica/epic_pirate.ogg')
pygame.mixer.music.set_volume(0.4)
pygame.mixer.music.play(-1,0.0)

# Efeitos sonoros
som_tesouro = pygame.mixer.Sound('assets/musica/registradora.ogg')
som_buraco = pygame.mixer.Sound('assets/musica/laugh.ogg')
som_fora = pygame.mixer.Sound('assets/musica/no.ogg')
som_vitoria = pygame.mixer.Sound('assets/musica/aplausos.ogg')
som_empate = pygame.mixer.Sound('assets/musica/vaia.ogg')


# Loop da Tela inicial
tela_inicial()
run_tela_inicial = True
while run_tela_inicial:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            run_tela_inicial = False
            pygame.quit()
            sys.exit()
        if (evento.type == pygame.KEYDOWN) and (evento.key == pygame.K_RETURN):
            run_tela_inicial = False

# Loop da Tela de instruções
tela_instrucao()
run_tela_instrucao = True
while run_tela_instrucao:
    for evento in pygame.event.get():
        if (evento.type == pygame.QUIT):
            run_tela_instrucao = False
            pygame.quit()
            sys.exit()
        if (evento.type == pygame.KEYDOWN) and (evento.key == pygame.K_RETURN):
            run_tela_instrucao = False


def vez_jogador():
    global vez
    if vez == 'Jogador 1':
        vez = 'Jogador 2'
    else:
        vez = 'Jogador 1'
    return vez

# Randomização dos tesouros e buracos --> feito no randomizar.py

def main_game():
    global vez, dic_ponto, estado, ganhador, cor
    conteudo_celula = randomizar()
    vez = 'Jogador 1'
    dic_ponto = {'Jogador 1': 0, 'Jogador 2': 0}
    pontuacao = 0
    tela_jogo()

    pygame.mixer.music.load('assets/musica/uncharted.ogg')
    pygame.mixer.music.set_volume(0.4)
    pygame.mixer.music.play(-1,0.0)

    # Matriz revelação
    matriz_revelada = [[False for i in range(num_linhas)] for j in range(num_linhas)]
    num_celulas_abertas = 0
    running = True
    while running:

        for evento in pygame.event.get():

            if (evento.type == pygame.QUIT):
                running = False
                pygame.quit()
                sys.exit()

            tela_mudou = False

            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                # background da tela do jogo
                tela_jogo()

                # Pega as coordenadas do ponto de clique e calcula a celula
                mouse_x, mouse_y = evento.pos

                lin = mouse_x // celula_x - 1
                col = mouse_y // celula_y - 1

                # Clicou fora do tabuleiro
                if (lin > num_linhas - 1) or (lin == -1) or col == -1 or col > num_linhas-1 :
                    fora = pygame.image.load('assets/imagens/fora.png')
                    fora = pygame.transform.scale(fora, (5*celula_x, celula_y//2))
                    screen.blit(fora, (celula_x*3, 5*celula_y+celula_y/3-6))
                    som_fora.play()
                    som_fora.set_volume(0.35)
                    continue

                # Entra no if se a celula foi clicada pela primeira vez
                if (not matriz_revelada[col][lin]):
                    tela_mudou = True
                    num_celulas_abertas += 1
                    matriz_revelada[col][lin] = True

                    # verifica se é tesouro, buraco ou ajuda
                    if (conteudo_celula[col][lin] == "t"):
                        som_tesouro.play()
                        som_tesouro.set_volume(0.2)
                        pontuacao = 100

                    elif (conteudo_celula[col][lin] == "b"):
                        som_buraco.play()
                        som_buraco.set_volume(0.35)
                        if (dic_ponto[vez] <= 0):
                            pontuacao = 0
                        else:
                            pontuacao = -50
                    else:
                        pontuacao = 0

            if (tela_mudou):
                dic_ponto[vez] += pontuacao

                x,y = lin, col

                if (conteudo_celula[y][x] == "t"):
                    tesouro = pygame.image.load('assets/imagens/tesouro.png')
                    tesouro = pygame.transform.scale(tesouro, (celula_x - 2, celula_y - 2))
                    screen.blit(tesouro, (celula_x * (x+1), celula_y * (y+1) ))
                elif (conteudo_celula[y][x] == "b"):
                    buraco = pygame.image.load('assets/imagens/buraco.png')
                    buraco = pygame.transform.scale(buraco, (celula_x - 2, celula_y - 2))
                    screen.blit(buraco, (celula_x * (x + 1), celula_y * (y+1)))
                else:
                    texto = fonte.render(conteudo_celula[y][x], False, preto)
                    screen.blit(texto, (borda_x_e*0.4+ celula_x * (x + 1), borda_y*1.3 + celula_y * y + (y+1)))

                vez_jogador()

            for x in range(num_linhas):
                for y in range(num_linhas):
                    if matriz_revelada[y][x] == True:
                        if (conteudo_celula[y][x] == "t"):
                            tesouro = pygame.transform.scale(tesouro, (celula_x - 2, celula_y - 2))
                            screen.blit(tesouro, (celula_x * (x + 1), celula_y * (y + 1)))
                        elif (conteudo_celula[y][x] == "b"):
                            buraco = pygame.transform.scale(buraco, (celula_x - 2, celula_y - 2))
                            screen.blit(buraco, (celula_x * (x + 1), celula_y * (y + 1)))
                        else:
                            texto = fonte.render(conteudo_celula[y][x], False, preto)
                            screen.blit(texto, (borda_x_e * 0.4 + celula_x * (x + 1), borda_y * 1.3 + celula_y * y + (y + 1)))

                pygame.display.flip()

            show_player(vez,celula_x, celula_y/3)
            show_score(dic_ponto)
            pygame.display.update()

            #condição finalizar jogo
            if (num_celulas_abertas == num_linhas ** 2 ):
                sleep(0.55)
                running = False

    vencedor(dic_ponto)
    menu_final()


def menu_final():
    # background
    tela_final()

    # botoes rect em preto
    botao_credito = pygame.Rect(celula_x // 2 - 5, 5 * celula_y + 3, 136, 37)
    botao_reiniciar = pygame.Rect(3 * celula_x, 4 * celula_y + 65, 60, 60)
    pygame.draw.rect(screen, preto, botao_credito, border_radius=5)
    pygame.draw.rect(screen, preto, botao_reiniciar, border_radius=35)

    # sobreposição figura botoes (surface)
    botao_cred = pygame.image.load('assets/imagens/botao_creditos.png')
    botao_cred = pygame.transform.scale(botao_cred, (2 * celula_x, 2 * celula_y))
    screen.blit(botao_cred, (celula_x // 2 - 10, 4 * celula_y + celula_y // 3))
    botao_rein = pygame.image.load('assets/imagens/botao_reiniciar.png')
    botao_rein = pygame.transform.scale(botao_rein, (celula_x * 3 // 2, 3 * celula_y // 2))
    screen.blit(botao_rein, (3 * celula_x - 25, 4 * celula_y + 41))

    click = False
    while True:
        mx, my = pygame.mouse.get_pos()
        if botao_credito.collidepoint((mx, my)):
            if click == True:
                tela_creditos()
        if botao_reiniciar.collidepoint((mx, my)):
            if click == True:
                main_game()

        click = False
        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (evento.type == pygame.KEYDOWN) and (evento.key == pygame.K_RETURN):
                pygame.quit()
                sys.exit()
            if (evento.type == pygame.MOUSEBUTTONDOWN and evento.button == 1):
                click = True
        pygame.display.update()

main_game()