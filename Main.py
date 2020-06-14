import pygame
from lib.pygame_functions import *
import math
from Game import Game
from Monster import Pics
from player import Player

pygame.init()

#charger le jeu
game = Game()

#Affichage écran
pygame.display.set_caption("Sonic")
screen = pygame.display.set_mode((game.W,game.H))

background = pygame.image.load("img/Green_Hill.png")

piegeBackground = Pics(game)

#Position de l'image
x = 0

#Coordonnées play_button
play_button_x_min = 371
play_button_x_max = 648
play_button_y_min = 249
play_button_y_max = 347

#importer/charger la bannière
banner = pygame.image.load("img/Banniere/banner0.jpg")
banner = pygame.transform.scale(banner, (game.W,game.H))
banner_rect = banner.get_rect()

#########

running = True


#################
testSprite = makeSprite("img/running/SonicSprite_resized.gif", 32)

moveSprite(testSprite,300,300,True)
showSprite(testSprite)

nextFrame = clock()
frame = 0


#Boucle tant que condition est vraie
while running:

	if clock() > nextFrame:
		frame = (frame+1)%8
		nextFrame += 80

	if keyPressed(K_d):
		changeSpriteImage(testSprite, 0*8+frame)

	elif keyPressed(K_q):
		changeSpriteImage(testSprite, 2*8+frame)

	else:
		game.player.image = pygame.image.load("img/SonicStatiqueRight.png")

	#Appliquer l'arrère plan et le faire bouger
	relative_x = game.background_origin_x % background.get_rect().width
	screen.blit(background, (relative_x - background.get_rect().width,0))
	if relative_x < game.W:
			screen.blit(background,(relative_x,0))

	#vérifier si le jeu a commencé
	if game.is_playing:
		#délencher les instructions de la partie
		game.update(screen)
	#vérifier si le jeu n'a pas commencé
	else:
		#ajouter l'écran de bienvenue
		screen.blit(banner, banner_rect)

	#Mise a jour de la fenêtre
	pygame.display.flip()

	#Si le joueur ferme la fenêtre
	for event in pygame.event.get():
		#vérifier la fermeture de la fenêtre
		if event.type == pygame.QUIT:
			running = False
			pygame.quit()

		#detecter si une touche du clavier est laché
		elif event.type == pygame.KEYDOWN:
			game.pressed[event.key] = True

			#détecter si la touche espace est enclanchée pour lancer le projectile
			if event.key == pygame.K_SPACE:
				game.player.launch_projectile()

		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

		elif event.type == pygame.MOUSEBUTTONDOWN:
			x_mouse, y_mouse = pygame.mouse.get_pos()
			#Vérification si clique sur le bouton
			if x_mouse > play_button_x_min and x_mouse < play_button_x_max and y_mouse < play_button_y_max and y_mouse > play_button_y_min :
				#mettre le jeu en mode "lancé"
				game.start()