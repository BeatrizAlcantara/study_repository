# 81 Faça um programa que leia vários números e coloque em uma lista. Depois mostre: quantos números foram digitados; a lista de valores ordenada de forma decrescente; se o valor 5 foi digitado e está ou não na lista.

def Main081():
    lista = [];
    resposta = 'S'
    while resposta in 'Ss':
        numero = int(input('Digite um numero: '))
        lista.append(numero)
        resposta = input('Deseja continuar? [S/N] ')
    lista.sort(reverse=True)

    print(f'A lista tem {len(lista)} numeros.')
    print(f'A lista digitada foi: {lista}.')

    if 5 in lista:
       print('O valor 5 está presente na lista.')
    else:
        print('O valor 5 não está presente na lista.')

Main081()