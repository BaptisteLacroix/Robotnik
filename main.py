from party import Party
from monster import Pic
from player import Player
from menu import Menu
import pygame

pygame.init()

# Affichage écran
pygame.display.set_caption("Sonic")
screen = pygame.display.set_mode((Party.W, Party.H))
print(screen)

background = pygame.image.load("img/Green_Hill.png")



# Position de l'image
x = 0

##############

# charger le jeu
party = Party()
player = Player(party)
menu = Menu(screen)

###########
piegeBackground = Pic(party)

#lance le menu
menu.loop()

###############

frame = 0

# Boucle tant que condition est vraie
while party.running:

    keys = pygame.key.get_pressed()
    party.player.process_movement_animation(keys)

    # Mise a jour de la fenêtre
    pygame.display.flip()

    for event in pygame.event.get():
        # detecter si une touche du clavier est laché
        if event.type == pygame.KEYDOWN:
            party.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                print("saut")
                Player.jump(player)

            if event.key == pygame.K_ESCAPE:
                party.is_playing = False
                screen.blit(menu.banner, menu.banner_rect)

        elif event.type == pygame.KEYUP:
            party.pressed[event.key] = False

            for event in pygame.event.get():
                if event.type == pygame.MOUSEBUTTONDOWN:
                    # détecter si le click gauche est enclanché pour lancer le projectile
                    if party.is_playing and pygame.mouse.get_pressed()[0]:
                        party.player.launch_projectile()

#################
"""
frame = 0

# Boucle tant que condition est vraie
while game.running:

    keys = pygame.key.get_pressed()
    game.player.process_movement_animation(keys)

    # Appliquer l'arrère plan et le faire bouger
    relative_x = game.background_origin_x % background.get_rect().width
    screen.blit(background, (relative_x - background.get_rect().width, 0))
    if relative_x < game.W:
        screen.blit(background, (relative_x, 0))

    # vérifier si le jeu a commencé
    if game.is_playing:
        # délencher les instructions de la partie
        game.update(screen)
    # vérifier si le jeu n'a pas commencé
    else:
        # ajouter l'écran de bienvenue
        screen.blit(banner, banner_rect)


    # Mise a jour de la fenêtre
    pygame.display.flip()

    for event in pygame.event.get():
        # vérifier la fermeture de la fenêtre
        if event.type == pygame.QUIT:
            game.is_playing = False
            pygame.quit()

        # detecter si une touche du clavier est laché
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                print("saut")
                Player.jump(player)

            if event.key == pygame.K_ESCAPE:
                game.is_playing = False
                screen.blit(banner, banner_rect)

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            # Vérification si clique sur le bouton
            if not game.is_playing and play_button_x_min < x_mouse < play_button_x_max and play_button_y_max > y_mouse > play_button_y_min:
                # mettre le jeu en mode "lancé"
                game.start()
            # détecter si le click gauche est enclanché pour lancer le projectile
            elif game.is_playing and pygame.mouse.get_pressed()[0]:
                game.player.launch_projectile()
"""