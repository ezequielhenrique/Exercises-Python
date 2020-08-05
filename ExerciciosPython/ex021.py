# Programa em Python que abre e reproduz o áudio de um arquivo MP3.

import pygame
pygame.mixer.init()     # Inicializando o mixer Pygame
pygame.init()           # Inicializando o Pygame

pygame.mixer.music.load('champions.mp3')
pygame.mixer.music.play()
pygame.event.wait()

print('Fim!')
