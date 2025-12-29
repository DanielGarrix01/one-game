import pygame
import data.images.cards.loader as card_loader
from data.menu import main_menu

version = 1.0

pygame.init()
width, height = 1920, 1080
screen = pygame.display.set_mode((width, height), pygame.NOFRAME)
pygame.display.set_caption(f"ONE Game - v{version}")

def main():
    if __debug__:
        print("ONE is running...")
    # Iniciar con el menú principal
    main_menu(screen, width, height)
    pygame.quit()

if __name__ == "__main__":
    main()
