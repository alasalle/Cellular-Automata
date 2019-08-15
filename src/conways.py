import pygame
import random
import numpy as np
 
# Define some colors and other constants
RED = (255,0,0)
SILVER = (192,192,192)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GREEN = (0, 255, 0)
WIN_SIZE = 600
CELL_SIZE = 25
MARGIN = 5

world = np.random.choice(a=[0, 1], size=(WIN_SIZE // CELL_SIZE + MARGIN, WIN_SIZE // CELL_SIZE + MARGIN))

pygame.init()
 
# Set the width and height of the screen [width, height]
size = (WIN_SIZE, WIN_SIZE)
screen = pygame.display.set_mode(size)

# Add a title
pygame.display.set_caption("Conway's Game of Life")
 
# Loop until the user clicks the close button.
done = False
 
# Used to manage how fast the screen updates
clock = pygame.time.Clock()
 
# -------- Main Program Loop -----------
while not done:
    # --- Main event loop
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True
 
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
    newWorld = np.copy(world)
    for (x, y), value in np.ndenumerate(world):
        newWorld[x, y] = cell_next_gen(x, y, world)
        if newWorld[x, y] == 1:
            pygame.draw.rect(screen, WHITE, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), MARGIN)
            pygame.draw.rect(screen, GREEN, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), 0)

        else:
            pygame.draw.rect(screen, WHITE, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), MARGIN)
            pygame.draw.rect(screen, SILVER, (CELL_SIZE * (x - 1), CELL_SIZE * (y - 1), CELL_SIZE, CELL_SIZE), 0)


    world = newWorld

    # --- Go ahead and update the screen with what we've drawn.
    pygame.display.flip()
 
    # --- Limit to 5 frames per second
    clock.tick(5)
 
# Close the window and quit.
pygame.quit()