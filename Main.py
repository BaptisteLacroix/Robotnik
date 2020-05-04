import pygame
from Game import Game
pygame.init()



#Affichage écran
pygame.display.set_caption("Sonic")
screen = pygame.display.set_mode((1080,720))
background = pygame.image.load("FondSonic.png")

#charger le jeu
game = Game()


running = True

#Boucle tant que condition est vraie
while running:

	#Appliquer l'arrère plan
	screen.blit(background, (0,0))

	#appliquer l'image du joueur
	screen.blit(game.player.image, game.player.rect)

	# vérifier si le joeuur veut aller à gauche ou à droite
	if game.pressed.get(pygame.K_d) and game.player.rect.x < 850:
		game.player.move_right()

	elif game.pressed.get(pygame.K_q) and game.player.rect.x > -90:
		game.player.move_left()
	elif game.pressed.get(pygame.K_SPACE):
		game.player.move_up()

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


