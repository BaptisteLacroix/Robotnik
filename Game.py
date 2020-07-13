import pygame
from player import Player
from Monster import Pics

run_right_path = "img/running/right/SonicRun"
img_extension = ".png"


# Classe qui représente le jeu
class Game:
    W = 1022
    H = 498
    runRight = [pygame.image.load(run_right_path + str(i) + img_extension) for i in range(8)]

    def __init__(self):
        # définir si le jeu a commencé ou non
        self.is_playing = False
        # position du fond
        self.background_origin_x = 0
        # générer le joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        # Groupe de pics
        self.all_pics = pygame.sprite.Group()
        self.pressed = {}

    def start(self):
        self.is_playing = True
        self.spawn_pics()
        self.spawn_pics()

    def game_over(self):
        # remettre le jeu à zéro
        self.all_pics = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupérer les monstres de mon jeu
        for Pics in self.all_pics:
            Pics.forward()
            Pics.update_health_bar(screen)

        # ppliquer l'image des projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de pics
        self.all_pics.draw(screen)

        # vérifier si le joueur veut aller à gauche, à droite ou sauter
        if self.pressed.get(pygame.K_d):
            if self.player.rect.x < Game.W * 4 / 10:
                right = True
            if self.player.rect.x < Game.W * 4 / 10:
                self.player.move_right()
            else:
                self.background_origin_x -= 5

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_pics(self):
        pics = Pics(self)
        self.all_pics.add(pics)
