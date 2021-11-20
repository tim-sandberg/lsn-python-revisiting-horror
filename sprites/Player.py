import pygame


class Player(pygame.sprite.Sprite):
    """
        
    """
    images = []
    
    def __init__(self, screen_rectangle):
        """
        this is the constructor!
        """
        
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.SCREENRECT = screen_rectangle

        self.image = self.images[0]

        self.image_size = self.image.get_size()

        self.rect = self.image.get_rect(center=(800, 400))
        