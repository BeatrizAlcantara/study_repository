# 68. Faça um programa que jogue par ou ímpar com o computador. O jogo só será interrompido quando o jogador perder, mostrando o total de vitórias consecutivas que ele conquistou no final do jogo.

import random

def Main068():
    resultado = 'V'
    vitorias = jogadas = 0
    print('\nJOGO: PAR OU ÍMPAR\n')

    while(resultado == 'V'):
        jogadas += 1

        j_jogador = int(input('\n[0] Par ou [1] Ímpar? '))
        if j_jogador == 0:
            escolha_jogador = 'PAR'
        else:
            escolha_jogador = 'IMPAR'

        numero_jogador = int(input('Escolha seu número: '))
        numero_computador = random.randint(0, 10)
        soma_jogadas = numero_jogador + numero_computador
        

        print(f'\nJogadas: \n VOCÊ: {numero_jogador}\n COMPUTADOR: {numero_computador}\n Total: {soma_jogadas}.\n')
        
        if soma_jogadas%2 == 0 and escolha_jogador == 'PAR': # resultado par
            resultado = 'V'; vitorias += 1
            print('Ganhou!')
        elif soma_jogadas%2 == 1 and escolha_jogador == 'IMPAR': # resultado impar
            resultado = 'V'
            print('Ganhou!')
        else:
            print('Perdeu!')
            resultado = 'P'; break

    print(f'\nSeu total de vitorias foi: {vitorias}! De {jogadas} jogadas.')


Main068()

