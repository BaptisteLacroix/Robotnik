import pygame
import random

class Pics(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game = game
		self.attack = 30
		self.health = 50
		self.max_health = 50
		self.velocity = random.randint(1,3)
		self.image = pygame.image.load("img/PicMonstre1.png")
		self.rect = self.image.get_rect()
		self.rect.x = 900 + random.randint(0,300)
		self.rect.y = 300

	def damage(self, amount):
		#infliger les dégats
		self.health -= amount

		#vérifier si son nouveau nombre de points de vie est inférieur ou égal à 0
		if self.health <= 0:
			# Réapparaitre comme un nouveau piège
			self.rect.x = 900 + random.randint(0,300)
			self.velocity = random.randint(1,3)
			self.health = self.max_health


	def update_health_bar(self, surface):
		#dessiner la barre de vie
		pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 10, self.rect.y - 10, self.max_health, 5])
		pygame.draw.rect(surface, (238, 158, 20), [self.rect.x + 10, self.rect.y - 10, self.health, 5])


	def forward(self):
		#déplacement se fait que si il n'y a pas de collision  avec un groupe de joueur
		if not self.game.check_collision(self, self.game.all_players):
			self.rect.x -= self.velocity
		#Si le monstre est en collision avec le joueur
		else:
			#infliger des dégats
			self.game.player.damage(self.attack)
			self.rect.x = 900 + random.randint(0,300)
			self.velocity = random.randint(1,3)
			self.health = self.max_health