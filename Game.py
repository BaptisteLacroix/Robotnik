import pygame
from player import Player
from Monster import Pics

#Classe qui représente le jeu
class Game:

	def __init__(self):
		#générer le joueur
		self.player = Player(self)
		#Groupe de pics
		self.all_pics = pygame.sprite.Group()
		self.player = pygame.sprite.Group()
		self.pressed = {}
		self.spawn_pics()

	def check_collision(self, sprite, Group):
		return pygame.sprite.spritecollide(sprite, Group, True, pygame.sprite.collide_mask)


	def spawn_pics(self):
		pics = Pics()
		self.all_pics.add(pics)