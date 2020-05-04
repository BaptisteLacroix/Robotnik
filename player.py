import pygame

#Joueur Sonic
class Player(pygame.sprite.Sprite):

	def __init__(self):
		super().__init__()
		#self.health = 100
		#self.max_health = 100
		self.velocity = 5
		self.image = pygame.image.load("Sonic.png")
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 350


	def move_right(self):
		self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity

	def move_up(self):
		self.rect.y -= self.velocity