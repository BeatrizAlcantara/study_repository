# 77 Faça um programa que tenha uma tupla com várias palavras (sem acentos), e que deverá mostrar, para cada palavra, as suas vogais.

def Main077():
    t = ('batom', 'brinco', 'pente','anel')
    vogais = ('a', 'e', 'i', 'o', 'u')

    for i in t:
        print(f'\nVogais de {i}: ', end='')
        for j in range(len(i)):
            if i[j] in vogais:
                print(f'{i[j]}', end='')

Main077()


