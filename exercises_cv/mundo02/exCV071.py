# Faça um programa que simule o funcionamento de um caixa eletrônico. Pergunte qual será o valor a ser sacado (número inteiro) e o programa vai informar quantas cédulas de cada valor serão entregues. Considere cédulas de 50, 20, 10 e 1.

def Main071():
    valor_total = int(input('Qual o valor do saque? R$ '))

    notas_50 = valor_total // 50; resto = valor_total % 50;
    notas_20 = resto // 20; resto = resto % 20;
    notas_10 = resto // 10; resto = resto % 10;

    print(f'Serão entregues:\n - {notas_50} notas de 50;\n - {notas_20} notas de 20;')
    print(f' - {notas_10} notas de 10;\n - {resto} notas de 1;')


Main071()
