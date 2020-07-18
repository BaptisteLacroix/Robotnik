from party import Party
from menu import Menu
import pygame


def main():
    pygame.init()
    # Affichage écran
    pygame.display.set_caption("Sonic")
    screen = pygame.display.set_mode((Party.W, Party.H))
    # charger le jeu
    menu = Menu(screen)
    # lance le menu
    menu.loop()


if __name__ == '__main__':
    main()
