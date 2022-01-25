# 75 Faça um programa que leia 4 valores e guarde-os em uma tupla. No final, mostre: quantas vezes apareceu o número 9; em qual posição foi digitado o primeiro valor 3; e quais foram os números pares.

def Main075():
    a = int(input('Digite um numero: ')); b = int(input('Digite um numero: '))
    c = int(input('Digite um numero: ')); d = int(input('Digite um numero: '))
    t = (a, b, c, d)
    
    print(f'Tupla: {t}.')
    print(f'Numero 9 apareceu {t.count(9)} vezes.')

    if 3 not in t:
        print('Numero 3 nao foi digitado.')
    else:
        print(f'Numero 3 foi digitado primeiro na {t.index(3)+1}º posicao.')

    print('Numeros pares foram: ')
    for i in range(len(t)):
        if (t[i] % 2 == 0):
            print(f'{t[i]} ')

Main075()

