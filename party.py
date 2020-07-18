import pygame
from player import Player
from monster import Pic

run_right_path = "img/running/right/SonicRun"
img_extension = ".png"
background = pygame.image.load("img/Green_Hill.png")


# Classe qui représente le jeu
class Party:
    """
    Une partie contenant un joueur, des pièges et des projectiles en mouvements.
    """
    W = 1022
    H = 498
    runRight = [pygame.image.load(run_right_path + str(i) + img_extension) for i in range(8)]
    is_playing = False

    def __init__(self):
        """
        Initialise une partie en créant:
            - un joueur,
            - deux groupes contenant respectivement les joueurs de la partie et les futurs projectiles
        """
        # définir si le jeu a commencé ou non
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
        Party.is_playing = True
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
        print("GameOver")
        Party.is_playing = False

    def move_background(self, screen):
        """

        :param screen: Surface sur laquelle afficher les éléments graphiques.
        :return:
        """
        relative_x = self.background_origin_x % background.get_rect().width
        screen.blit(background, (relative_x - background.get_rect().width, 0))
        if relative_x < self.W:
            screen.blit(background, (relative_x, 0))

    def update_player(self, screen):
        """

        :param screen:
        :return:
        """
        keys = pygame.key.get_pressed()
        events = pygame.event.get()

        for event in events:
            # detecter si une touche du clavier est laché
            if event.type == pygame.KEYDOWN:
                self.pressed[event.key] = True

                if event.key == pygame.K_SPACE:
                    print("saut")
                    Player.jump(self.player)  # TODO: move in update_player

                if event.key == pygame.K_ESCAPE:
                    self.game_over()

            elif event.type == pygame.KEYUP:
                self.pressed[event.key] = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                # détecter si le click gauche est enclanché pour lancer le projectile
                if Party.is_playing and pygame.mouse.get_pressed()[0]:
                    self.player.launch_projectile()  # TODO: move in update_player

        self.player.update_health_bar(screen)
        screen.blit(self.player.image, self.player.rect) # TODO: check position
        self.player.process_movement_animation(keys)
        if self.pressed.get(pygame.K_d):
            if self.player.rect.x < Party.W * 4 / 10:
                right = True
            if self.player.rect.x < Party.W * 4 / 10:
                self.player.move_right()
            else:
                self.background_origin_x -= 5

    def update_pics(self, screen):
        """

        :param screen:
        :return:
        """
        for pic in self.all_pics:
            pic.forward(self)
            pic.update_health_bar(screen)
        self.all_pics.draw(screen)

    def update_projectiles(self, screen):
        """

        :param screen:
        :return:
        """
        for projectile in self.player.all_projectiles:
            projectile.move()
        self.player.all_projectiles.draw(screen)

    def loop(self, screen):
        """
        Met a jour les composants (Barre de vie, projectiles, etc...) de la partie.
        :param screen: Surface sur laquelle afficher les éléments graphiques.
        :return:
        """
        # Appliquer l'arrère plan et le faire bouger
        self.move_background()
        # actualise les éléments graphiques
        self.update_projectiles(screen)
        self.update_pics(screen)
        self.update_player(screen)

        # détecter si le click gauche est enclanché pour lancer le projectile
        if pygame.mouse.get_pressed()[0]:
            self.player.launch_projectile() # TODO: move in update_player


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
        pics = Pic()
        self.all_pics.add(pics)
