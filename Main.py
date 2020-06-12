import pygame
from Game import Game
from Monster import Pics
from player import Player

pygame.init()


#Affichage écran
pygame.display.set_caption("Sonic")
W = 1022
H = 498
screen = pygame.display.set_mode((W,H))

background = pygame.image.load("img/Green_Hill.png")
piegeBackground = Pics()

#Position de l'image
x = 0

#charger le jeu
game = Game()


running = True

#Boucle tant que condition est vraie
while running:

	#Appliquer l'arrère plan et le faire bouger
	relative_x = x % background.get_rect().width
	screen.blit(background, (relative_x - background.get_rect().width,0))
	if relative_x < W:
			screen.blit(background,(relative_x,0))




	#appliquer l'image du joueur
	screen.blit(game.player.image, game.player.rect)



	#appliquer l'ensemble des images de mon groupe de pics
	game.all_pics.draw(screen)

"""
	#récupérer la barre de vie du joueur
	for Player in game.player:
		Player.update_health_bar(screen)
"""

	#recupérer les monstres de mon jeu
	for Pics in game.all_pics:
		Pics.forward()
		Pics.update_health_bar(screen)



	# vérifier si le joeuur veut aller à gauche ou à droite
	if game.pressed.get(pygame.K_d):
		if game.player.rect.x < W*4/10:
			game.player.image = pygame.image.load("img/SonicStatiqueRight.png")
			if game.player.rect.x < W*4/10:
				game.player.move_right()
		else:
			x -= 5

	elif game.pressed.get(pygame.K_a):
		game.player.image = pygame.image.load("img/SonicStatiqueLeft.png")
		if game.player.rect.x > W*4/10:
			game.player.move_left()
		else:
			x += 5

	"""elif game.pressed.get(pygame.K_SPACE):
		game.player.move_up()
	"""


	
	print(game.player.rect.x)




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
		elif event.type == pygame.KEYUP:
			game.pressed[event.key] = False

