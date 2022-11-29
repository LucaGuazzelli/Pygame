


import pygame, sys, random
pygame.init() 

Jogador_pontos = 0 
Adversario_pontos = 0 
fonte = pygame.font.SysFont("Free Sans Bold", 32)

sons = {'som1': 'mixkit-game-ball-tap-2073.wav'}

def play_sound(tipo_de_som):
	pygame.mixer.music.load(tipo_de_som)
	pygame.mixer.music.play()

def Bola_animacao():
	global Bola_vel_x, Bola_vel_y
	
	Bola .x += Bola_vel_x
	Bola .y += Bola_vel_y

	if Bola.top <= 0 or Bola.bottom >= Tela_altura:
		Bola_vel_y *= -1
	if Bola.left <= 0:
		bola_start()
		Jogador_pontos += 1
	if Bola.right >= Tela_largura:
		bola_start()
		Adversario_pontos += 1
	if Bola.colliderect(Jogador) or Bola.colliderect(Adversario):
		Bola_vel_x *= -1
		play_sound(sons['som1'])


def player_animation():
	Jogador.y += jogador_Vel

	if Jogador.top <= 0:
		Jogador.top = 0
	if Jogador.bottom >= Tela_altura:
		Jogador.bottom = Tela_altura 

def adversario():
	if Adversario.top < Bola.y:
		Adversario.y += Adversario_vel
	if Adversario.bottom > Bola.y:
		Adversario.y -= Adversario_vel

	if Adversario.top <= 0:
		Adversario.top = 0
	if Adversario.bottom >= Tela_altura:
		Adversario.bottom = Tela_altura

def bola_start():
	global Bola_vel_x, Bola_vel_y

	Bola.center = (Tela_largura/2, Tela_altura/2)
	Bola_vel_y *= random.choice((1,-1))
	Bola_vel_x *= random.choice((1,-1))

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

Bola_vel_x = 7 * random.choice((1,-1))
Bola_vel_y = 7 * random.choice((1,-1))
jogador_Vel = 0
Adversario_vel = 7
Bola_mex = False 
Tempo_pontos = True 


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
				
					
	if Tempo_pontos:
		bola_start()
	
		
	player_text = fonte.render(f'{Jogador_pontos}',False,Cor)
	Tela.blit(player_text,(660,470))

	opponent_text = fonte.render(f'{Adversario_pontos}',False,Cor)
	Tela.blit(opponent_text,(600,470))
	
	Bola_animacao()
	player_animation()
	adversario()

	Tela.fill('grey12')
	pygame.draw.rect(Tela, Cor, Jogador)
	pygame.draw.rect(Tela, Cor, Adversario)
	pygame.draw.ellipse(Tela, Cor, Bola )
	pygame.draw.aaline(Tela, Cor, (Tela_largura / 2, 0),(Tela_largura / 2, Tela_altura))

	pygame.display.flip()
	clock.tick(60)