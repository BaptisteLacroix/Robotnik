import pygame


# définir la classe qui va gérer le projectile de notre monstre
class Projectile(pygame.sprite.Sprite):
    """
    Des projectiles contenant toutes leur caractéristiques.
    """

    # définir le constructeur de cette classe
    def __init__(self, player):
        """
        Initalise le projectile en créant:
            - son image
            - ses points d'attaque
            - sa vitesse
        :param player:
        """
        super().__init__()
        self.velocity = 3
        self.player = player
        self.image = pygame.image.load("./img/projectile/projectile0.png")
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect = self.image.get_rect()
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 70
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        """
        Permet la rotation des projectiles.
        :return:
        """
        # tourner le projectile
        self.angle += 8
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        """
        Permet d'effacer les projectiles lors de la sortie de l'écran
        :return:
        """
        self.player.all_projectiles.remove(self)

    def move(self):
        """
        Permet de faire bouger les projectiles tant qu'ils ne sont pas en collision
        :return:
        """
        self.rect.x += self.velocity
        self.rotate()

        # vérifier si le projectile entre en collision avec un monstre
        for pic in self.player.game.check_collision(self, self.player.game.all_pics):
            # Supprimer le projectile
            self.remove()
            # infliger les dégats
            pic.damage(self.player.attack)

        # vérifier si le projectile n'est plus présent sur l'écran
        if self.rect.x > 1022:
            # supprimer le projectile
            self.remove()
            print("projectile supprimé")
