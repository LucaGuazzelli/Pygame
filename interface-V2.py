


import pygame, sys

def Bola_animacao():
	global Bola_vel_x, Bola_vel_y
	
	Bola .x += Bola_vel_x
	Bola .y += Bola_vel_y

	if Bola .top <= 0 or Bola .bottom >= Tela_altura:
		Bola_vel_y *= -1
	if Bola .left <= 0 or Bola .right >= Tela_largura:
		Bola_vel_x *= -1

	if Bola.colliderect(Jogador) or Bola.colliderect(Adversario):
		Bola_vel_x *= -1

def player_animation():
	Jogador.y += jogador_Vel

	if Jogador.top <= 0:
		Jogador.top = 0
	if Jogador.bottom >= Tela_altura:
		Jogador.bottom = Tela_altura 



pygame.init()
clock = pygame.time.Clock()

Tela_largura = 1200
Tela_altura = 500
Tela = pygame.display.set_mode((Tela_largura,Tela_altura))
pygame.display.set_caption('Jogo.Pygame - Luca, PH, Rafa')


Cor = (200,200,200)
bg_color = pygame.Color('grey12')



Bola  = pygame.Rect(Tela_largura / 2 - 15, Tela_altura / 2 - 15, 30, 30)
Jogador = pygame.Rect(Tela_largura - 20, Tela_altura / 2 - 70, 10,140)
Adversario = pygame.Rect(10, Tela_altura / 2 - 70, 10,140)

Bola_vel_x = 7
Bola_vel_y = 7
jogador_Vel = 0
Adversario_vel = 7




while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_UP:
					jogador_Vel -= 7
			if event.key == pygame.K_DOWN:
					jogador_Vel += 7
		if event.type == pygame.KEYUP:
				if event.key == pygame.K_UP:
					jogador_Vel += 7
				if event.key == pygame.K_DOWN:
					jogador_Vel -= 7
				
	Bola_animacao()
	player_animation()

	Tela.fill('grey12')
	pygame.draw.rect(Tela, Cor, Jogador)
	pygame.draw.rect(Tela, Cor, Adversario)
	pygame.draw.ellipse(Tela, Cor, Bola )
	pygame.draw.aaline(Tela, Cor, (Tela_largura / 2, 0),(Tela_largura / 2, Tela_altura))

	pygame.display.flip()
	clock.tick(60)