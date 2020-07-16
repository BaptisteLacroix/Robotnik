import pygame
from player import Player
from monster import Pic

run_right_path = "img/running/right/SonicRun"
img_extension = ".png"


# Classe qui représente le jeu
class Party:
    """
    Une partie contenant un joueur, des pièges et des projectiles en mouvements.
    """
    W = 1022
    H = 498
    runRight = [pygame.image.load(run_right_path + str(i) + img_extension) for i in range(8)]

    def __init__(self):
        """
        Initialise une partie en créant:
            - un joueur,
            - deux groupes contenant respectivement les joueurs de la partie et les futurs projectiles
        """
        # définir si le jeu a commencé ou non
        self.is_playing = False
        self.running = True
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
        """
        Permet le lancement de la partie avec l'apparition de 2 pièges (chaque piège détruit est renouvelé)
        :return:
        """
        self.is_playing = True
        self.spawn_pics()
        self.spawn_pics()

    def game_over(self):
        """
        Rénitialise le jeu lors de la mort du personnage.
        :return:
        """
        # TODO: remettre le jeu à zéro
        self.all_pics = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.is_playing = False

    def update(self, screen):
        """
        Met a jour les composants (Barre de vie, projectiles, etc...) de la partie.
        :param screen: Surface sur laquelle afficher les éléments graphiques.
        :return:
        """
        # Appliquer l'arrère plan et le faire bouger
        relative_x = self.background_origin_x % Party.background.get_rect().width
        screen.blit(Party.background, (relative_x - Party.background.get_rect().width, 0))
        if relative_x < self.W:
            screen.blit(Party.background, (relative_x, 0))

        # appliquer l'image du joueur
        screen.blit(self.player.image, self.player.rect)

        # Actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        # Récupérer les projectiles du joueur
        for projectile in self.player.all_projectiles:
            projectile.move()

        # recupérer les monstres de mon jeu
        for pic in self.all_pics:
            pic.forward()
            pic.update_health_bar(screen)

        # ppliquer l'image des projectiles
        self.player.all_projectiles.draw(screen)

        # appliquer l'ensemble des images de mon groupe de pics
        self.all_pics.draw(screen)

        # vérifier si le joueur veut aller à gauche, à droite ou sauter
        if self.pressed.get(pygame.K_d):
            if self.player.rect.x < Party.W * 4 / 10:
                right = True
            if self.player.rect.x < Party.W * 4 / 10:
                self.player.move_right()
            else:
                self.background_origin_x -= 5

        # détecter si le click gauche est enclanché pour lancer le projectile
        if self.is_playing and pygame.mouse.get_pressed()[0]:
            self.player.launch_projectile()

    def check_collision(self, sprite, group):
        """
        Vérifie et renvoie si le sprite donné entre en collision avec l'un des éléments du groupe (group) donné.
        :param sprite: élément graphique (Joueur, projectile, ...) dont l'on souhaite tester la collision
        :param group: Groupe contenant un ensemble d'éléments graphiques (pièges, ...)
        :return: s'il y a collision ou pas
        """
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_pics(self):
        """
        Crée un piège (Pic) et l'ajoute à l'ensemble des pièges existants.
        :return:
        """
        pics = Pic(self)
        self.all_pics.add(pics)
