import pygame
from time import sleep

class RevisitingHorrorGame:
    # a list of pygame Rects, representing all areas
    # changed on the screen
    all_game_rects = pygame.sprite.RenderUpdates()

    def main(self):
        # Initialize pygame
        if pg.get_sdl_version()[0] == 2:
            pg.mixer.pre_init(44100, 32, 2, 1024)
            
        pg.init()
        
        fullscreen = False
        # Set the display mode
        winstyle = 0  # |FULLSCREEN
        bestdepth = pg.display.mode_ok(SCREENRECT.size, winstyle, 32)
        screen = pg.display.set_mode(SCREENRECT.size, winstyle, bestdepth)
