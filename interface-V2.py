import pygame, sys, random
from pygame import mixer 
from pygame.locals import *
from pygame import mixer
from playsound import playsound
import os


pygame.init()
Tempo_pontos = True
Jogador_pontos = 0 
Adversario_pontos = 0 
#impotanado as fontes dos pontos 
fonte = pygame.font.SysFont("Free Sans Bold", 32)
tela_inicio = pygame.image.load('assets/tela1.jpeg')

#animacao da bola e para ela bater nas paredes 

def Bola_animacao():
	global Bola_vel_x, Bola_vel_y,Tempo_pontos,Adversario_pontos, Jogador_pontos
	
	Bola.x += Bola_vel_x
	Bola.y += Bola_vel_y

	if Bola.top <= 0 or Bola.bottom >= Tela_altura:
		Bola_vel_y *= -1
		
	if Bola.left <= 0:
		Tempo_pontos = pygame.time.get_ticks()
		Jogador_pontos += 1
		
	if Bola.right >= Tela_largura:
		Tempo_pontos = pygame.time.get_ticks()
		Adversario_pontos += 1
		

	if Bola.colliderect(Jogador) and Bola_vel_x > 0:
		
		if abs(Bola.right - Jogador.left) < 10:
			Bola_vel_x *= -1
			
		elif abs(Bola.bottom - Jogador.top) < 10 or abs(Bola.top - Jogador.bottom) < 10 :
			Bola_vel_y *= -1
			
	

	if Bola.colliderect(Adversario):
		if abs(Bola.left - Adversario.right) < 10 or abs(Bola.right - Jogador.left) < 10:
			Bola_vel_x *= -1	
		else:
			Bola_vel_y *= -1
#def do jogador 
def player_animation():
	Jogador.y += jogador_Vel

	if Jogador.top <= 0:
		Jogador.top = 0
	if Jogador.bottom >= Tela_altura:
		Jogador.bottom = Tela_altura 

#def que faz o ai exister e jogar contra o player 
def adversario():
	if Adversario.top < Bola.y:
		Adversario.y += Adversario_vel
	if Adversario.bottom > Bola.y:
		Adversario.y -= Adversario_vel

	if Adversario.top <= 0:
		Adversario.top = 0
	if Adversario.bottom >= Tela_altura:
		Adversario.bottom = Tela_altura
#def para fazer a bola comecar no lugar e comecar a bola e sua diercao 
def bola_start():
	global Bola_vel_y, Bola_vel_x, Bola_mex, Tempo_pontos, Cor

	Bola.center = (Tela_largura/2, Tela_altura/2)
	tempo = pygame.time.get_ticks()

	if tempo - Tempo_pontos < 700:
		number_three = fonte.render("3",False, Cor)
		Tela.blit(number_three,(Tela_largura/2 - 10, Tela_altura/2 + 20))
	if 700 < tempo - Tempo_pontos < 1400:
		number_two = fonte.render("2",False,Cor)
		Tela.blit(number_two,(Tela_largura/2 - 10, Tela_altura/2 + 20))
	if 1400 < tempo - Tempo_pontos < 2100:
		number_one = fonte.render("1",False,Cor)
		Tela.blit(number_one,(Tela_largura/2 - 10, Tela_altura/2 + 20))

	if tempo - Tempo_pontos < 2100:
		Bola_vel_x, Bola_vel_y = 0,0
	else:
		Bola_vel_x = 7 * random.choice((1,-1))
		Bola_vel_y = 7 * random.choice((1,-1))
		Tempo_pontos = None

def menu(tela):

	tela.blit(tela_inicio, (0, 0))

	return None

clock = pygame.time.Clock()
#size da tela 
Tela_largura = 1200
Tela_altura = 500
Tela = pygame.display.set_mode((Tela_largura,Tela_altura))
pygame.display.set_caption('Jogo.Pygame - Luca, PH, Rafa')


#variaveis de cada cor que vao ser usadas depois
Cor = (200,200,200)
bg_color = pygame.Color('grey12')

#lugar de cada item na tela do jogo
Bola  = pygame.Rect(Tela_largura / 2 - 15, Tela_altura / 2 - 15, 30, 30)
Jogador = pygame.Rect(Tela_largura - 20, Tela_altura / 2 - 70, 10,140)
Adversario = pygame.Rect(10, Tela_altura / 2 - 70, 10,140)

#variaveis
Bola_vel_x = 7 * random.choice((1,-1))
Bola_vel_y = 7 * random.choice((1,-1))
jogador_Vel = 0
Adversario_vel = 7
Bola_mex = False 

pygame.init() 
pygame.mixer.pre_init(44100, -16, 1, 512)
pygame.mixer.init()
pygame.mixer.music.load("musica1.wav")

menu_inicial = True

while True:
	jogo_start = False 
	#para fachar o programa
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()
			sys.exit()
		#comando que o jogador faz
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

		#Jogo tocar musica 
		pygame.mixer.music.play()
		pygame.display.update()
	#Jogo stop depois de 6 pontos 
	if Jogador_pontos > 5 or Adversario_pontos > 5:
		pygame.quit()
	

				
	
		
	Bola_animacao()
	player_animation()
	adversario()

	#para criara os item que estao no jogo 
	Tela.fill('grey12')
	pygame.draw.rect(Tela, Cor, Jogador)
	pygame.draw.rect(Tela, Cor, Adversario)
	pygame.draw.ellipse(Tela, Cor, Bola )
	pygame.draw.aaline(Tela, Cor, (Tela_largura / 2, 0),(Tela_largura / 2, Tela_altura))


	if Tempo_pontos:
		bola_start()
	#para escrver os pontos
	player_text = fonte.render(f'{Jogador_pontos}',False,Cor)
	Tela.blit(player_text,(1000,47))

	opponent_text = fonte.render(f'{Adversario_pontos}',False,Cor)
	Tela.blit(opponent_text,(67,47))

	pygame.display.flip()
	clock.tick(60)


