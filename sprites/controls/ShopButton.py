import pygame

from sprites.controls.Button import Button

class ShopButton(pygame.sprite.Sprite):
    """
    """
    images = []

    def __init__(self, screen_rectangle):
        pygame.sprite.Sprite.__init__(self, self.containers)

        self.SCREENRECT = screen_rectangle

        # null check the images list
        if(len(self.images) > 0):
            self.image = self.images[0]

            self.image_size = self.image.get_size()

            self.rect = self.image.get_rect(center=(800, 400))
    
    def visibility(self, can_show):
        if(can_show is True):
            self.image = self.images[0]
        else:
            self.image = self.images[1]
    
    def button_clicked(self):
        hitbox = self.rect.inflate(-5, -5)

        return hitbox.colliderect