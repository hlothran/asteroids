import pygame
from constants import *
from player import *

def main():
    #added for bootdev purposes
    print("Starting asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")

    # pygom initialize
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
    clock = pygame.time.Clock()
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
        
        screen.fill("black")

        clock.tick(FPS_LIMITER) #limit FPS to 60

        player_x = SCREEN_WIDTH/2
        player_y = SCREEN_HEIGHT/2
        player = Player(player_x, player_y)

        player.draw(screen)

        pygame.display.flip()

if __name__ == "__main__":
    main()
