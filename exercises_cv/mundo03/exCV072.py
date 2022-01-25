# 72 Faça um programa que tenha um tupla totalmente preenchida com uma contagem por extenso, de zero a vinte. O programa deverá ler um número pelo teclado (entre 0 e 20) e mostra-lo por extenso.

def Main072():
    numeros = ('zero', 'um', 'dois', 'tres', 'quatro', 'cinco', 'seis', 'sete', 'oito', 'nove', 'dez', 'onze', 'doze', 'treze', 'quartoze', 'quinze', 'dezesseis', 'dezessete', 'dezoito', 'dezenove', 'vinte')

    n = int(input('Digite um numero de 0 a 20: '))

    print(f'Voce escolheu o numero: {numeros[n]}.')


Main072()
