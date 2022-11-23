# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame, random 

from Ball import bola, jogador, adversario, cor, screen_height, screen_width  

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Bate volta - Luca, Rafa e PH')

# ----- Inicia estruturas de dados
game = True

    # vel da bola 

Vel_bola_x = 1 * random.choice((1,-1))
vel_bola_y = 1 * random.choice((1,-1))
vel_jogador = 0 
vel_adversario = 7

def bola_restart():
    bola_centro = (screen_width/2, screen_height/2)
    vel_bola_y = vel_bola_y * random.choice((1,-1))
    Vel_bola_x = Vel_bola_x * random.choice((1,-1))
    
# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT or event.type == pygame.KEYUP:
            game = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                vel_jogador = vel_jogador + 7
            if event.key == pygame.K_UP:
                vel_jogador = vel_jogador - 7
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                vel_jogador = vel_jogador - 7
            if event.key == pygame.K_UP:
                vel_jogador = vel_jogador + 7
                
                

    bola.x = bola.x + Vel_bola_x
    bola.y = bola.y + vel_bola_y
    jogador_y = vel_jogador + jogador_y


    if adversario.top < bola.y:
        bola.top = bola.top + vel_adversario
    if adversario.bottom > bola.y:
        bola.top = bola.top - vel_adversario

    if adversario.top <= 0:
        adversario.top = 0
    if adversario.bottom >= screen_height:
        adversario.bottom = screen_height


    if jogador.top <= 0:
        jogador.top = 0
    if jogador.bottom >= screen_height:
        jogador.bottom = screen_height

    if bola.top  <= 0 or bola.bottom >= screen_height:
        vel_bola_y = vel_bola_y * -1 
    if bola.left <= 0 or bola.right >= screen_width:
        bola_restart()
    


    if bola.collidedict(jogador) or bola.collidedict(adversario):
        Vel_bola_x = Vel_bola_x + - 1


    # ----- Gera saídas
    window.fill((228, 228, 228))

    # Desenho da Bola E OUTROS 
    pygame.draw.rect(window, cor, jogador) 
    pygame.draw.rect(window,cor,adversario)
    pygame.draw.ellipse(window,cor, bola)
    pygame.draw.aaline(window,cor,(screen_width/2,0), screen_width/2,screen_height)



    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

