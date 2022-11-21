import pygame, sys 

screen_width = 600
screen_height = 300
screen = pygame.display.set_mode((screen_width, screen_height))

bola = pygame.Rect(screen_width/2 - 15, screen_height/2 - 15,30,30)
jogador = pygame.Rect(screen_width - 20, screen_height/2 - 70,10,140)
adversario = pygame.Rect(10, screen_height/2 - 70,10,140)
cor = (0,0,128)




