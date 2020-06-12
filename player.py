import pygame


#jump_height = 50

#Joueur Sonic
class Player(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game = game
		self.attack = 50
		self.health = 30
		self.max_health = 30
		self.velocity = 2
		self.image = pygame.image.load("img/SonicStatiqueRight.png")
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 200
		#self.jumping = False
		#self.jump_offset = 0

	def move_right(self):
		if not self.game.check_collision(self, self.game.all_pics):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity

	def move_up(self):
		self.rect.y -= self.velocity

"""


	def update_health_bar(self, surface):
		# définir une couleur pour la barre de vie
		bar_color = (229, 25, 25)
		#définir une couleur pour l'arrière plan de la barre
		back_bar_color = (60, 63, 60)

		# définir la position de la barre de vie, sa largeur et son épaisseur
		bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
		#définir la position de l'arrère plan de la jauge de vie
		back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

		#dessiner la barre de vie
		pygame.draw.rect(surface, back_bar_color, back_bar_position)
		pygame.draw.rect(surface, bar_color, bar_position)

 
"""


		"""

	def do_jumping(Player):
		global jump_height

		if Player.jumping:
			Player.jump_offset += 1
			if Player.jump_offset >= jump_height:
				Player.jumping = False
		elif Player.jump_offset > 0 and Player.jumping == False:
			Player.jump_offset -= 1


elif game.pressed.get(pygame.K_SPACE) and player.jumping == False and player.jump_offset == 0:
		player.jumping = True

		"""
