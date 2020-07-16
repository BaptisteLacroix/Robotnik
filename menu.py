import pygame
from party import Party

game = Party()


class Menu:
    """
    Un menu permettant de lancer le jeu ou de partir dans les options.
    """

    # Coordonnées play_button
    play_button_x_min = 371
    play_button_x_max = 648
    play_button_y_min = 249
    play_button_y_max = 347

    # importer/charger la bannière
    banner = pygame.image.load("img/Banniere/banner0.jpg")
    banner = pygame.transform.scale(banner, (game.W, game.H))
    banner_rect = banner.get_rect()
    bannerPartyOver = pygame.image.load("img/Banniere/bannerPartyOver.jpg")

    #########

    def __init__(self, screen):
        """
        Initialise le menu en créant:
            - Le bouton play
            - le bouton des paramètres
        :param screen: Surface sur laquelle afficher les éléments graphiques.
        """
        self.is_active = True
        self.screen = screen

    def loop(self):
        """
        Boucle permettant de faire tourner le menu avec :
            - Le bouton Play
            - Le chargement de la fenêtre
        :return:
        """
        while self.is_active:
            self.screen.blit(Menu.banner, Menu.banner_rect)

            for event in pygame.event.get():
                # vérifier la fermeture de la fenêtre
                if event.type == pygame.QUIT:
                    game.is_playing = False
                    pygame.quit()

                if event.type == pygame.MOUSEBUTTONDOWN:
                    x_mouse, y_mouse = pygame.mouse.get_pos()
                    # Vérification si clique sur le bouton
                    if not game.is_playing and Menu.play_button_x_min < x_mouse < Menu.play_button_x_max and Menu.play_button_y_max > y_mouse > Menu.play_button_y_min:
                        # mettre le jeu en mode "lancé"
                        game.start()

            # vérifier si le jeu a commencé
            if game.is_playing:
                # délencher les instructions de la partie
                game.update(self.screen)
            # vérifier si le jeu n'a pas commencé
            else:
                # ajouter l'écran de bienvenue
                self.screen.blit(Menu.banner, Menu.banner_rect)
