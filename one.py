import pygame
import data.images.cards.loader as card_loader

version = 1.0

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.display.set_caption(f"ONE Game - v{version}")

def main():
    running = True
    if __debug__:
        print("ONE is running...")
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running = False
        pygame.display.flip()
    pygame.quit()

if __name__ == "__main__":
    main()
