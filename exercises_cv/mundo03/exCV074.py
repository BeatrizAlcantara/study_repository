# 74 Faça um programa que gere 5 números aleatórios em uma tupla, depois mostre a listagem de números gerados e indique o maior e menor valor na tupla.
import random

def Main074():
    a = random.randint(0,100); b = random.randint(0,100)
    c = random.randint(0,100); d = random.randint(0,100)
    e = random.randint(0,100)
    t = (a, b, c, d, e)
    print(f'Tupla: {t}.')
    print(f'Maior numero: {max(t)}. E menor numero: {min(t)}.')

Main074()