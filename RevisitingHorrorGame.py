import pygame
from pygame.locals import Rect
from time import sleep

from common import Constants
from common import Utility
from sprites.Player import Player
from sprites.controls.Button import Button
from sprites.controls.ShopButton import ShopButton


class RevisitingHorrorGame:
    # a list of pygame Rects, representing all areas
    # changed on the screen
    all_game_rects = pygame.sprite.RenderUpdates()

    # assign default groups to each sprite class
    ShopButton.containers = all_game_rects

    main_menu_screen_background = pygame.Surface(
        Constants.SCREEN_RECTANGLE.size)

    def main(self):
        # Initialize pygame
        if pygame.get_sdl_version()[0] == 2:
            pygame.mixer.pre_init(44100, 32, 2, 1024)

        pygame.init()

        fullscreen = False
        # Set the display mode
        window_style = 0  # |FULLSCREEN
        bestdepth = pygame.display.mode_ok(
            Constants.SCREEN_RECTANGLE.size, window_style, 32)

        # This function will create a display Surface
        # Initialize a window or screen for display
        screen = pygame.display.set_mode(
            Constants.SCREEN_RECTANGLE.size, window_style, bestdepth)

        self.set_game_obj_images(screen)

        # game sound enabled
        self.set_game_sound()

        # assign default groups to each sprite class
        Player.containers = self.all_game_rects

        clock = self.game_loop(screen, self.main_menu_screen_background)

        self.quit_game()

    def set_game_obj_images(self, screen):
        """
            Load images, assign to sprite classes
            (do this before the classes are used, after screen setup)
        """
        print("RevisitingHorrorGame - set_game_obj_images()")

        main_menu_background_image = Utility.load_image(
            "revisiting_horror_main_background.jpg")

        self.set_background(
            screen, self.main_menu_screen_background, main_menu_background_image)

        pygame.display.set_caption("Revisiting Horror")

        # Update the full display Surface to the screen
        pygame.display.flip()

    def set_transparent_image_on_game_object(self, image_names, game_object):
        for image_name in image_names:
            image_surface = Utility.load_image_transparent_background(
                image_name)

            game_object.images.append(image_surface)

    def set_game_sound(self):
        print("RevisitingHorrorGame - set_game_sound()")

        # check for sound
        if pygame.mixer and not pygame.mixer.get_init():
            print("Warning, no sound")
            pygame.mixer = None

        # ambience-creepy-wind.wav
        Utility.load_music("rpg-battle-loop-1.wav")

    def set_background(self, screen, background, background_image):
        # blit: draws one image (Surface) on top of another (Surface)
        background.blit(background_image, (0, 0))

        # Draws a source Surface onto this Surface
        screen.blit(background, (0, 0))

    def game_loop(self, screen, background):
        clock = pygame.time.Clock()
        self.set_transparent_image_on_game_object(
            ["shop button.png"], Player)
        player = Player(Constants.SCREEN_RECTANGLE)
        self.do_main_menu_screen(self.all_game_rects, background, screen)

        print("Is player alive: ", player.alive())

        while (player.alive() is True):

            # clear/erase the last drawn sprites by painting over with
            # backdrop
            self.all_game_rects.clear(screen, background)

            # update all the sprites.  call all Sprites' update()
            self.all_game_rects.update()

        return clock

    def do_main_menu_screen(self, all_game_rects, background, screen):
        print("RevisitingHorrorGame - do_main_menu_screen(), ")

        self.set_transparent_image_on_game_object(
            ["shop button.png"], ShopButton)

        # 1. get shop and play button surfaces
        shop_button = ShopButton(Constants.SCREEN_RECTANGLE)

        # 2. show buttons on screen
        shop_button.rect = shop_button.image.get_rect(center=(0, 500))

        shop_button.visibility(True)

        # update all the sprites.  call all Sprites' update()
        self.all_game_rects.update()

        # draw the scene
        self.all_game_rects.draw(screen)
        pygame.display.update()

        # cap the framerate
        # clock.tick(60)

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
