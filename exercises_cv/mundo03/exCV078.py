# 78 Faça um programa que leia 5 valores numéricos e guarde-os em uma lista. No final, mostre qual foi o maior e o menor valor digitado e as suas respectivas posições na lista.

def Main078():
    lista = []; maior = -9999999; menor = 9999999
    for i in range (5):
        numero = int(input('Digite um numero: '))
        lista.append(numero)
        if numero > maior:
            maior = numero 
        if numero < menor:
            menor = numero

    print(f'A lista digitada foi: {lista}.')
    print(f'O maior numero foi {maior} e o menor foi {menor}.')

Main078()