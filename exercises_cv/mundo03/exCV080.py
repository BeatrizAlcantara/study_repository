# 80 Faça um programa onde o usuário possa digitar 5 valores numéricos e cadastre-os em uma lista, já na posição correta de inserção (sem usar o sort()). No final, mostre a lista ordenada na tela.

def Main080():
    lista = [];
    for i in range(6):
        numero = int(input('Digite um numero: '))
        if i == 0 or numero > lista[-1]:
            lista.append(numero)
        else:
            posicao = 0
            while posicao < len(lista):
                if numero <= lista[posicao]:
                    lista.insert(posicao, numero)
                    break
                posicao += 1

    print(f'A lista digitada foi: {lista}.')

Main080()