# ===== Inicialização =====
# ----- Importa e inicia pacotes
import pygame

from Ball import bola, jogador, adversario, cor  

pygame.init()

# ----- Gera tela principal
window = pygame.display.set_mode((600, 300))
pygame.display.set_caption('Bate volta - Luca, Rafa e PH')

# ----- Inicia estruturas de dados
game = True

# ===== Loop principal =====
while game:
    # ----- Trata eventos
    for event in pygame.event.get():
        # ----- Verifica consequências
        if event.type == pygame.QUIT or event.type == pygame.KEYUP:
            game = False

    # ----- Gera saídas
    window.fill((228, 228, 228))

    # Desenho da Bola 
     pygame.draw.rect(window, cor, jogador)  

    # ----- Atualiza estado do jogo
    pygame.display.update()  # Mostra o novo frame para o jogador

# ===== Finalização =====
pygame.quit()  # Função do PyGame que finaliza os recursos utilizados

