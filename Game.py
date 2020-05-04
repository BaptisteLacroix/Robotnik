import pygame
from player import Player

#Classe qui représente le jeu
class Game:

	def __init__(self):
		#générer le joueur
		self.player = Player()
		self.pressed = {}
