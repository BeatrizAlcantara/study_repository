#21. Faça um programa que abra e reproduza o áudio de um arquivo MP3.

import pygame #vscode - pip install pygame

def Main021():
    print('É hora de chorar..')
    pygame.init()
    pygame.mixer.music.load('music.mp3')
    pygame.mixer.music.play()
    pygame.event.wait()

Main021()