import pygame
import random
import numpy as np
 
# Define some colors and other constants
RED = (255,0,0)
SILVER = (192,192,192)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)

WIN_SIZE = 500
CELL_SIZE = 20
MARGIN = 5

world = np.random.choice(a=[0, 1], size=(WIN_SIZE// CELL_SIZE + MARGIN, WIN_SIZE// CELL_SIZE + MARGIN))
currentWorld = world
generation = 1
fps = 1
pygame.init()
 
# Set the width and height of the screen [width, height]
size = (520, 655)
screen = pygame.display.set_mode(size)

fasterButton = pygame.Rect(100, 100, 123.75, 50)
slowerButton = pygame.Rect(100, 100, 123.75, 50)
togglePlayButton = pygame.Rect(100, 100, 123.75, 50)
restartButton = pygame.Rect(100, 100, 123.75, 50)

fasterButton.x = 5
fasterButton.y = 600
slowerButton.x = 133.75
slowerButton.y = 600
togglePlayButton.x = 262.5
togglePlayButton.y = 600
restartButton.x = 391.25
restartButton.y = 600

# Add a title
pygame.display.set_caption('Conway\'s Game of Life Generation')
 
# Loop until the user clicks the close button.
done = False
state = 'RUNNING'
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
        if event.type == pygame.MOUSEBUTTONDOWN:
                mouse_pos = event.pos

                if fasterButton.collidepoint(mouse_pos):
                    fps += 1
                if slowerButton.collidepoint(mouse_pos):
                    if fps > 1:
                        fps -= 1
                if togglePlayButton.collidepoint(mouse_pos):
                    if state == 'RUNNING':
                        state = 'PAUSED'
                    elif state == 'PAUSED':
                        state = 'RUNNING'
                if restartButton.collidepoint(mouse_pos):
                    world = np.random.choice(a=[0, 1], size=(WIN_SIZE// CELL_SIZE + MARGIN, WIN_SIZE// CELL_SIZE + MARGIN))
                    generation = 0
 
    # --- Game logic should go here
    def cell_next_gen(x, y, world):
        neighbours = np.sum(world[x - 1: x + 2, y - 1: y + 2]) - world[x, y]
        if world[x, y] == 1 and not 2 <= neighbours <= 3:
            return 0
        elif neighbours == 3:
            return 1
        return world[x, y]

 
    # --- Screen-clearing code goes here
 
    # Here, we clear the screen to gray. Don't put other drawing commands
    # above this, or they will be erased with this command.
    screen.fill(WHITE)
 
    # --- Drawing code should go here
    if state == 'RUNNING':

        newWorld = np.copy(world)
        for (x, y), value in np.ndenumerate(world):
            newWorld[x, y] = cell_next_gen(x, y, world)
            if newWorld[x, y] == 1:
                pygame.draw.rect(screen, WHITE, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), MARGIN)
                pygame.draw.rect(screen, GREEN, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), 0)

            else:
                pygame.draw.rect(screen, WHITE, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), MARGIN)
                pygame.draw.rect(screen, SILVER, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), 0)

            currentWorld = newWorld
        
        pygame.draw.rect(screen, GREEN, fasterButton)
        pygame.draw.rect(screen, GREEN, slowerButton)
        pygame.draw.rect(screen, GREEN, togglePlayButton)
        pygame.draw.rect(screen, GREEN, restartButton)

        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        fasterButtonText = font.render("FASTER", True, BLACK)
        slowerButtonText = font.render("SLOWER", True, BLACK)
        togglePlayButtonText = font.render("PLAY/PAUSE", True, BLACK)
        restartButtonText = font.render("RESTART", True, BLACK)

        fasterText_rect = fasterButtonText.get_rect()
        fasterText_rect.center = fasterButton.center
        screen.blit(fasterButtonText, fasterText_rect)

        slowerText_rect = slowerButtonText.get_rect()
        slowerText_rect.center = slowerButton.center
        screen.blit(slowerButtonText, slowerText_rect)

        togglePlayText_rect = togglePlayButtonText.get_rect()
        togglePlayText_rect.center = togglePlayButton.center
        screen.blit(togglePlayButtonText, togglePlayText_rect)

        restartText_rect = restartButtonText.get_rect()
        restartText_rect.center = restartButton.center
        screen.blit(restartButtonText, restartText_rect)
        
        genFont = pygame.font.Font(pygame.font.get_default_font(), 16)
        genText = genFont.render(f'Generation: {generation} - FPS: {fps}', True, BLACK)
        screen.blit(genText, ((screen.get_width() - genText.get_width())/2, (screen.get_height() - 73)))


        world = newWorld
        generation = generation + 1

        # --- Go ahead and update the screen with what we've drawn.
        pygame.display.flip()
        

        # --- Limit to 5 frames per second
        clock.tick(fps)

    elif state == 'PAUSED':
        for (x, y), value in np.ndenumerate(currentWorld):
            if currentWorld[x, y] == 1:
                pygame.draw.rect(screen, WHITE, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), MARGIN)
                pygame.draw.rect(screen, GREEN, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), 0)

            else:
                pygame.draw.rect(screen, WHITE, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), MARGIN)
                pygame.draw.rect(screen, SILVER, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), 0)
            
        pygame.draw.rect(screen, GREEN, fasterButton)
        pygame.draw.rect(screen, GREEN, slowerButton)
        pygame.draw.rect(screen, GREEN, togglePlayButton)
        pygame.draw.rect(screen, GREEN, restartButton)

        font = pygame.font.Font(pygame.font.get_default_font(), 20)
        fasterButtonText = font.render("FASTER", True, BLACK)
        slowerButtonText = font.render("SLOWER", True, BLACK)
        togglePlayButtonText = font.render("PLAY/PAUSE", True, BLACK)
        restartButtonText = font.render("RESTART", True, BLACK)

        fasterText_rect = fasterButtonText.get_rect()
        fasterText_rect.center = fasterButton.center
        screen.blit(fasterButtonText, fasterText_rect)

        slowerText_rect = slowerButtonText.get_rect()
        slowerText_rect.center = slowerButton.center
        screen.blit(slowerButtonText, slowerText_rect)

        togglePlayText_rect = togglePlayButtonText.get_rect()
        togglePlayText_rect.center = togglePlayButton.center
        screen.blit(togglePlayButtonText, togglePlayText_rect)

        restartText_rect = restartButtonText.get_rect()
        restartText_rect.center = restartButton.center
        screen.blit(restartButtonText, restartText_rect)
        
        genFont = pygame.font.Font(pygame.font.get_default_font(), 16)
        genText = genFont.render(f'Generation: {generation} - FPS: {fps}', True, BLACK)
        screen.blit(genText, ((screen.get_width() - genText.get_width())/2, (screen.get_height() - 73)))

        world = currentWorld



 
# Close the window and quit.
pygame.quit()