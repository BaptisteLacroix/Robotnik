from Game import Game
from Monster import Pics
from player import Player
import pygame

pygame.init()

# charger le jeu
game = Game()

# Affichage écran
pygame.display.set_caption("Sonic")
screen = pygame.display.set_mode((game.W, game.H))

background = pygame.image.load("img/Green_Hill.png")

piegeBackground = Pics(game)

# Position de l'image
x = 0

# Coordonnées play_button
play_button_x_min = 371
play_button_x_max = 648
play_button_y_min = 249
play_button_y_max = 347

# importer/charger la bannière
banner = pygame.image.load("img/Banniere/banner0.jpg")
banner = pygame.transform.scale(banner, (game.W, game.H))
banner_rect = banner.get_rect()
bannerGameOver = pygame.image.load("img/Banniere/bannerGameOver.jpg")

#########

running = True

#################

frame = 0

# Boucle tant que condition est vraie
while running:

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
            running = False
            pygame.quit()

        # detecter si une touche du clavier est laché
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                Player.jump(self)

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
