import random
from display import *

def randomizar():
    global conteudo_celula
    num_tesouro = 0
    num_buraco = 0
    conteudo_celula = [[None for i in range(num_linhas)] for j in range(num_linhas)]

    # colocar tesouros:
    while (num_tesouro < 6):
        i = random.randint(0, num_linhas - 1)  # -1 por ser intervalo fechado [0,3]
        j = random.randint(0, num_linhas - 1)
        if (conteudo_celula[i][j] == None):
            conteudo_celula[i][j] = "t"
            num_tesouro += 1

    # colocar buracos
    while (num_buraco < 3):
        i = random.randint(0, num_linhas - 1)  # -1 por ser intervalo fechado [0,3]
        j = random.randint(0, num_linhas - 1)
        if conteudo_celula[i][j] == None:
            conteudo_celula[i][j] = 'b'
            num_buraco += 1

    # Contagem de tesouros na vizinhaça:
    for i in range(0, num_linhas):
        for j in range(0, num_linhas):
            if (conteudo_celula[i][j] != 't' and conteudo_celula[i][j] != 'b'):
                n_t_ao_redor = 0

                # Acima
                if (i - 1 >= 0 and conteudo_celula[i - 1][j] == 't'):
                    n_t_ao_redor += 1
                # Esquerda
                if (j - 1 >= 0 and conteudo_celula[i][j - 1] == 't'):
                    n_t_ao_redor += 1
                # Direita
                if (j + 1 < num_linhas and conteudo_celula[i][j + 1] == 't'):
                    n_t_ao_redor += 1
                # Abaixo
                if (i + 1 < num_linhas and conteudo_celula[i + 1][j] == 't'):
                    n_t_ao_redor += 1

                conteudo_celula[i][j] = str(n_t_ao_redor)

    # for i in range(0, 4):
    #     print(conteudo_celula[i])
    return conteudo_celula
