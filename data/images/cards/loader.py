import pygame
import os

def load_backside(mode):
    """
    Carga la imagen del reverso de carta según el modo actual.
    """
    path = os.path.join("data", "images", "cards", "others", f"{mode}_backside.png")
    return pygame.image.load(path).convert_alpha()
