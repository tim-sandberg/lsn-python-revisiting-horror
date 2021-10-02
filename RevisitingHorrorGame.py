import pygame
from time import sleep

from common import Constants
from common import Utility

class RevisitingHorrorGame:
    # a list of pygame Rects, representing all areas
    # changed on the screen
    all_game_rects = pygame.sprite.RenderUpdates()

    main_menu_screen_background = pygame.Surface(Constants.SCREEN_RECTANGLE.size)

    def main(self):
        # Initialize pygame
        if pygame.get_sdl_version()[0] == 2:
            pygame.mixer.pre_init(44100, 32, 2, 1024)
            
        pygame.init()
        
        fullscreen = False
        # Set the display mode
        window_style = 0  # |FULLSCREEN
        bestdepth = pygame.display.mode_ok(Constants.SCREEN_RECTANGLE.size, window_style, 32)
        
        # This function will create a display Surface
        # Initialize a window or screen for display
        screen = pygame.display.set_mode(Constants.SCREEN_RECTANGLE.size, window_style, bestdepth)

        self.set_game_obj_images(screen)

        # game sound enabled
        self.set_game_sound()

        self.quit_game()

    
    def set_game_obj_images(self, screen):
        """
            Load images, assign to sprite classes
            (do this before the classes are used, after screen setup)
        """
        print("RevisitingHorrorGame - set_game_obj_images()")

        main_menu_background_image = Utility.load_image("revisiting_horror_main_background.jpg")

        self.set_background(screen, self.main_menu_screen_background, main_menu_background_image)

        pygame.display.set_caption("Revisiting Horror")

        # Update the full display Surface to the screen
        pygame.display.flip()

    def set_game_sound(self):
        print("RevisitingHorrorGame - set_game_sound()")

        # check for sound
        if pygame.mixer and not pygame.mixer.get_init():
            print("Warning, no sound")
            pygame.mixer = None

        Utility.load_music("rpg-battle-loop-1.wav")

    def set_background(self, screen, background, background_image):
        # blit: draws one image (Surface) on top of another (Surface)
        background.blit(background_image, (0, 0))

        # Draws a source Surface onto this Surface
        screen.blit(background, (0, 0))

    def do_main_menu_screen(self, screen):
        clock = pygame.time.Clock()
        
        return clock

    def quit_game(self):
        # if pygame sound is running
        if (pygame.mixer is not None):
            # for 1 second = 1000 milliseconds
            pygame.mixer.music.fadeout(1000)

        pygame.time.wait(1000)

        pygame.quit()

        # quit python
        quit()

# starting point for our game
if(__name__ == "__main__"):
    RevisitingHorrorGame().main()