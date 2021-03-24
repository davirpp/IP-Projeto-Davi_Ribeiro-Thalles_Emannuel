import pygame
from display import *
from cores import *
import sys

screen = pygame.display.set_mode((borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y*2))

def tela_inicial():
    global screen
    screen = pygame.display.set_mode((borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y*2))
    tela_ini = pygame.image.load('assets/imagens/tela_inicial.png')
    tela_ini = pygame.transform.scale(tela_ini, (borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y*2))
    screen.blit(tela_ini, (0,0))
    pygame.display.update()

def tela_instrucao():
    global screen
    screen = pygame.display.set_mode((borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y*2))
    tela_ini = pygame.image.load('assets/imagens/tela_instruc.png')
    tela_ini = pygame.transform.scale(tela_ini, (borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y*2))
    screen.blit(tela_ini, (0,0))
    pygame.display.update()


def tela_jogo():
    global screen
    screen = pygame.display.set_mode((borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y * 2))
    tela_main = pygame.image.load('assets/imagens/tela_jogo.png')
    tela_main = pygame.transform.scale(tela_main, (borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y * 2))
    screen.blit(tela_main, (0, 0))

    fundo_transp = pygame.image.load('assets/imagens/transparencia25p.png')
    fundo_transp = pygame.transform.scale(fundo_transp, (num_linhas*celula_x,num_linhas*celula_y))
    screen.blit(fundo_transp, (borda_x_e,borda_y))

    fundo_transp1 = pygame.image.load('assets/imagens/transparencia25p.png')
    fundo_transp1 = pygame.transform.scale(fundo_transp1, (num_linhas * celula_x, num_linhas * celula_y))
    screen.blit(fundo_transp1, (2*borda_x_e + num_linhas*celula_x, borda_y))

    pygame.draw.rect(screen, preto, (2*borda_x_e + num_linhas*celula_x, borda_y, 4* celula_x, 2*celula_y), 2)
    pygame.draw.rect(screen, preto, (2 * borda_x_e + num_linhas * celula_x, borda_y+2*celula_y, 4 * celula_x, 2 * celula_y), 2)

    for i in range(0, num_linhas):
       for j in range(0, num_linhas):
           pygame.draw.rect(screen, preto, (borda_x_e + i*celula_x, borda_y + j*celula_y, celula_x, celula_y), 2)

    pygame.display.flip()

def show_player(vez, x,y):
    pirata_fonte = pygame.font.Font("assets/fonte/Caribbean.ttf", 30)
    var = pirata_fonte.render(f'Vez = {vez}', True, preto)
    screen.blit(var, (x,y))

def show_score(dic_ponto):
    pirata_fonte = pygame.font.Font("assets/fonte/Caribbean.ttf", 30)
    fonte = pygame.font.SysFont("Comic Sams MS", 50)
    player1 = pirata_fonte.render('Jogador 1', True, vermelho)
    screen.blit(player1, (2*borda_x_e + num_linhas*celula_x + celula_x - 10, borda_y + celula_y/3))

    caveira = pygame.image.load('assets/imagens/coin_pirate.png')
    caveira = pygame.transform.scale(caveira, (celula_x - 10, celula_y - 10))
    screen.blit(caveira, (2*borda_x_e + num_linhas*celula_x + celula_x + 5, borda_y + celula_y))

    soma1 = fonte.render(f"{dic_ponto['Jogador 1']}", True, vermelho)
    screen.blit(soma1, (2*borda_x_e + num_linhas*celula_x + 2*celula_x + 10, borda_y + celula_y + celula_y/3 - 10))

    player2 = pirata_fonte.render('Jogador 2', True, azul)
    screen.blit(player2, (2 * borda_x_e + num_linhas * celula_x + celula_x - 10, borda_y + 2*celula_y + celula_y / 3))

    screen.blit(caveira, (2 * borda_x_e + num_linhas * celula_x + celula_x + 5, borda_y + 2*celula_y+ celula_y))

    soma2 = fonte.render(f"{dic_ponto['Jogador 2']}", True, azul)
    screen.blit(soma2, (2 * borda_x_e + num_linhas * celula_x + 2 * celula_x + 10, borda_y + celula_y+2*celula_y + celula_y / 3 - 10))


def vencedor(dic_ponto):
    global estado, ganhador, cor
    if dic_ponto['Jogador 1'] == dic_ponto['Jogador 2']:
        estado = 'Empate!'
        ganhador = ''
        cor = preto
    elif dic_ponto['Jogador 1'] > dic_ponto['Jogador 2']:
        estado = 'Vencedor:'
        ganhador = 'Jogador 1'
        cor = vermelho
    else:
        estado = 'Vencedor:'
        ganhador = 'Jogador 2'
        cor = azul

def tela_final():
    global screen, estado, cor, ganhador
    som_vitoria = pygame.mixer.Sound('assets/musica/aplausos.ogg')
    som_empate = pygame.mixer.Sound('assets/musica/vaia.ogg')
    pirata_fonte_f = pygame.font.Font("assets/fonte/Caribbean.ttf", 50)
    # vencedor()
    screen = pygame.display.set_mode((borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y * 2))
    tela_final = pygame.image.load('assets/imagens/tela_final.png')
    tela_final = pygame.transform.scale(tela_final, (borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y * 2))
    screen.blit(tela_final, (0, 0))

    # blit vencedor
    if estado == 'Empate!':
        som_empate.play()
        vencedor = pirata_fonte_f.render(estado, True, cor)
        screen.blit(vencedor, (2 * borda_x_e + num_linhas * celula_x - celula_x/2 + 30, borda_y - 20))
        fig_empate = pygame.image.load('assets/imagens/empate.png')
        fig_empate = pygame.transform.scale(fig_empate, (3 * celula_x - 25, 3 * celula_y - 10))
        screen.blit(fig_empate, (2 * borda_x_e + num_linhas * celula_x, borda_y + celula_y))

    else:
        som_vitoria.play()
        vencedor = pirata_fonte_f.render(estado, True, cor)
        screen.blit(vencedor, (2 * borda_x_e + num_linhas * celula_x - celula_x / 2 - 10, borda_y - 20))
        fig_vit = pygame.image.load('assets/imagens/vencedor_tesouro.png')
        fig_vit = pygame.transform.scale(fig_vit, (3 * celula_x , 3 * celula_y))
        screen.blit(fig_vit, (2 * borda_x_e + num_linhas * celula_x - 15, borda_y + celula_y//2 +10))

    # blit nome jogador
    blit_player = pirata_fonte_f.render(ganhador, True, cor)
    screen.blit(blit_player, (2 * borda_x_e + num_linhas * celula_x - celula_x/2, 5*borda_y - 30 ))

    pygame.display.update()

def botoes():
    global botao_credito, botao_reiniciar
    botao_credito = pygame.Rect(celula_x // 2 - 5, 5 * celula_y + 3, 136, 37)
    botao_reiniciar = pygame.Rect(3 * celula_x, 4 * celula_y + 65, 60, 60)

    pygame.draw.rect(screen, preto, botao_credito, border_radius=5)
    pygame.draw.rect(screen, preto, botao_reiniciar, border_radius=35)

    botao_cred = pygame.image.load('assets/imagens/botao_creditos.png')
    botao_cred = pygame.transform.scale(botao_cred, (2 * celula_x, 2 * celula_y))
    screen.blit(botao_cred, (celula_x // 2 - 10, 4 * celula_y + celula_y // 3))

    botao_rein = pygame.image.load('assets/imagens/botao_reiniciar.png')
    botao_rein = pygame.transform.scale(botao_rein, (celula_x * 3 // 2, 3 * celula_y // 2))
    screen.blit(botao_rein, (3 * celula_x - 25, 4 * celula_y + 41))

def tela_creditos():
    running = True
    while running:
        tela_cred = pygame.image.load('assets/imagens/tela_creditos.png')
        tela_cred = pygame.transform.scale(tela_cred, (borda_x_e + num_linhas * celula_x + borda_x_d, num_linhas * celula_y + borda_y * 2))
        screen.blit(tela_cred, (0, 0))

        for evento in pygame.event.get():
            if (evento.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if (evento.type == pygame.KEYDOWN) and (evento.key == pygame.K_ESCAPE):
                tela_final()
                botoes()
                running = False
        pygame.display.update()