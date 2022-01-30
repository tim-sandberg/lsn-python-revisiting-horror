import pygame
from sprites.controls.Button import Button

class PlayButton(pygame.sprite.Sprite):
    """
    """
    # def __init__(self, screen_rectangle):
    #     super().__init__(screen_rectangle)"""
    # This is a button control
    # """
    images = []
    
    def __init__(self, screen_rectangle):
        """
        this is the constructor for the Button class
        """
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.SCREENRECT = screen_rectangle

        if(len(self.images) > 0):
            self.image = self.images[0]

            self.image_size = self.image.get_size()

            self.rect = self.image.get_rect(center=(800, 400))

        # self.layer = 1

    def visibility(self, can_show):
        if(can_show is True):
            self.image = self.images[0]
        else:
            self.image = self.images[1]