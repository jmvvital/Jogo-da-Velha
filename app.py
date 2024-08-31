from random import randrange
import os
import time

def criar_tabuleiro():
    tabuleiro = [[' ' for _ in range(3)] for _ in range(3)]
    return tabuleiro

def imprimir_tabuleiro(tabuleiro):
     for line in tabuleiro:
        print('|'.join(line))
        print('-' * 5)

def verificar_jogada(jogada_linha, jogada_coluna, tabuleiro):
    if jogada_linha >= 3 or jogada_coluna >= 3 or tabuleiro[jogada_linha] [jogada_coluna] == 'X' or tabuleiro[jogada_linha] [jogada_coluna] == 'O':
        return False
    else:
        return True
    
def jogada(jogada_linha, jogada_coluna, jogador):
    tabuleiro[jogada_linha][jogada_coluna] = jogador

def verificar_vitoria(tabuleiro):
    if tabuleiro[0][0] == 'X' and tabuleiro[0][1] == 'X' and tabuleiro[0][2] == 'X' or tabuleiro[0][0] == 'O' and tabuleiro[0][1] == 'O' and tabuleiro[0][2] == 'O':
        return True
    if tabuleiro[1][0] == 'X' and tabuleiro[1][1] == 'X' and tabuleiro[1][2] == 'X' or tabuleiro[1][0] == 'O' and tabuleiro[1][1] == 'O' and tabuleiro[1][2] == 'O':
        return True

# Cria o tabuleiro
tabuleiro = criar_tabuleiro()

# Imprime o tabuleiro
imprimir_tabuleiro(tabuleiro)

jogador1_nome = input('Qual nome do Jogador 1? ')
jogador = 'X'
jogador2_nome = input('Qual nome do Jogador 2? ')
num_jogadas = 0
jogando = True

while num_jogadas < 9:
    if num_jogadas % 2 == 0:
        jogador = 'X'
        jogador_nome = jogador1_nome
        while jogando == True:
            jogada_linha = int(input(f'{jogador_nome}, em qual Linha deseja jogar? ')) - 1
            jogada_coluna = int(input(f'{jogador_nome}, em qual Coluna deseja jogar? ')) - 1
            if verificar_jogada(jogada_linha, jogada_coluna, tabuleiro) == False:
                print ('Campo Inválido ou já preenchido, tente novamente!')
            else:
                jogada(jogada_linha, jogada_coluna, jogador)
                num_jogadas +=1
                print ('Jogada Realizada!')
            break
            
        
    time.sleep(1)
    os.system("cls")
    imprimir_tabuleiro(tabuleiro)

    if num_jogadas % 2 != 0:
        jogador = 'O'
        jogador_nome = jogador2_nome
        while jogando == True:
            jogada_linha = int(input(f'{jogador_nome}, em qual Linha deseja jogar? ')) - 1
            jogada_coluna = int(input(f'{jogador_nome}, em qual Coluna deseja jogar? ')) - 1
            if verificar_jogada(jogada_linha, jogada_coluna, tabuleiro) == False:
                print ('Campo Inválido ou já preenchido, tente novamente!')
            else:
                jogada(jogada_linha, jogada_coluna, jogador)
                num_jogadas +=1
                print ('Jogada Realizada!')
            break
    
    time.sleep(1)
    os.system("cls")
    imprimir_tabuleiro(tabuleiro)







