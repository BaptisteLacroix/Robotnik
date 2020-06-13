import pygame
from projectile import Projectile


#jump_height = 50

#Joueur Sonic
class Player(pygame.sprite.Sprite):

	def __init__(self, game):
		super().__init__()
		self.game = game
		self.attack = 50
		self.health = 102
		self.max_health = 102
		self.velocity = 2
		self.all_projectiles = pygame.sprite.Group()
		self.image = pygame.image.load("img/SonicStatiqueRight.png")
		self.rect = self.image.get_rect()
		self.rect.x = 50
		self.rect.y = 200
		#self.jumping = False
		#self.jump_offset = 0

	def damage(self, amount):
		if self.health - amount > amount:
			self.health -= amount
		else:
			#si le joueur n'a plus de points de vie
			self.game.game_over()


	def update_health_bar(self, surface):
		#dessiner la barre de vie
		pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 15, self.rect.y - 20, self.max_health, 7])
		pygame.draw.rect(surface, (229, 25, 25), [self.rect.x + 15, self.rect.y - 20, self.health, 7])


	def launch_projectile(self):
		#créer une nouvelle instance de la classe projectile
		self.all_projectiles.add(Projectile(self))


	def move_right(self):
		if not self.game.check_collision(self, self.game.all_pics):
			self.rect.x += self.velocity

	def move_left(self):
		self.rect.x -= self.velocity

	def move_up(self):
		self.rect.y -= self.velocity



 

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
