import pygame
import sys

# Pygame initializations
pygame.init()
size_x = 800
size_y = 600
screen = pygame.display.set_mode((size_x, size_y))
pygame.display.set_caption("Sudoku con Hill Climbing")

# Global variables
gameRunning = True
showGameMenu = True

# Game Menu


def drawGameMenu():
    colour = (255, 255, 255)
    font = pygame.font.Font(None, 36)
    texts = ["SUDOKU CON ALGORÍTMO HILL CLIMBING", "Realizado por: ", "Marco Manrique Acha",
             "Elvia Bandida Arteaga", "Nicoll Malca", " ", "* Pulsa espacio para empezar *"]
    for i in range(len(texts)):
        text = font.render(texts[i], True, colour)
        screen.blit(text, (size_x/2 - text.get_width()/2,
                    size_y/4 - text.get_height()/2 + i*50))


# Game loop
while gameRunning:
    # Screen background
    screen.fill((191, 125, 59))
    # Check screen
    if showGameMenu:
        drawGameMenu()
    # Event handling
    for event in pygame.event.get():
        # Check if the user wants to quit
        if event.type == pygame.QUIT:
            gameRunning = False
        # Game Menu
        if showGameMenu == True:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    showGameMenu = False
        else:
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    showGameMenu = True
    # Update the screen
    pygame.display.update()

# Exit the game
pygame.display.quit()
sys.exit()
