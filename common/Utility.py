import os.path

import pygame

import common.Constants

# root of this revisiting horror project on the disk
main_directory = os.path.split(os.path.abspath(__file__))[0].replace("common", "", 1)


def rotate_surface(surface, rotation):
    """
    Sprite Surface is accessed: green_laser.image
    """
    surface = pygame.transform.rotate(surface, rotation)

    return surface


def load_image(file_name):
    """
    loads an image, prepares it for play
    """

    file_path_name = os.path.join(
        main_directory, common.Constants.IMAGES_PATH, file_name)

    try:
        surface = pygame.image.load(file_path_name)
    except pygame.error:
        raise SystemExit('Could not load image: ' + file_path_name)

        # raise SystemExit('Could not load image "%s" %s' %
        #                  (file_path_name, pygame.get_error()))

    return surface.convert()


def load_images(*file_names):
    """
    loading animation (multiple images for same sprite)
    """
    images = []

    for file_name in file_names:
        # we call load_image ^^^^^ above this function
        image = load_image(file_name)

        images.append(image)

    return images


def load_image_transparent_background(file_name, sub_folder=None):
    """
    loads an image with transparent background, prepares it for play

    https://www.pygame.org/docs/ref/image.html#pygame.image.load
    """

    if(sub_folder is None):
        file_path_name = os.path.join(
            main_directory, Constants.IMAGES_PATH, file_name)
    else:
        file_path_name = os.path.join(
            main_directory, sub_folder, file_name)

    try:
        surface = pygame.image.load(file_path_name)
    except pygame.error:
        raise SystemExit('Could not load image: ' + file_path_name)

        # raise SystemExit('Could not load image "%s" %s' %
        #                  (file_path_name, pygame.get_error()))

    return surface.convert_alpha()


class DummySound:
    def play(self):
        pass


def load_sound(file_name):
    # if pygame's mixer (sound) functionality isn't available
    # then return an empty DummySound object
    if (pygame.mixer is None):
        print("Utility - load_sound(), system found pygame mixer disabled.")

        return DummySound()

    file_name = os.path.join(main_directory, Constants.SOUNDS_PATH, file_name)

    try:
        # retrieve a pygame sound object
        sound = pygame.mixer.Sound(file_name)

        return sound
    except pygame.error:
        print('Warning, unable to load, %s' % file_name)

    return DummySound()
