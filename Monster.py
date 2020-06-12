import pygame

class Pics(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		self.attack = 10
		self.health = 50
		self.max_health = 50
		self.velocity = 1
		self.image = pygame.image.load("img/PicMonstre1.png")
		self.rect = self.image.get_rect()
		self.rect.x = 900
		self.rect.y = 350

	def damage(self, amount):
		#infliger les dégats
		self.health -= amount

		#vérifier si son nouveau nombre de points de vie est inférieur ou égal à 0
		if self.health <= 0:
			# Réapparaitre comme un nouveau piège
			self.rect.x = 900

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


	def forward(self):
		self.rect.x -= self.velocity