import os
import pygame
from pygame.locals import  Rect

current_directory = os.getcwd()
home_path = os.environ._data["HOMEDRIVE"] + os.environ._data["HOMEDRIVE"]

DISPLAY_WIDTH = 1024
DISPLAY_HEIGHT = 768

IMAGES_PATH = "data\\images"
MAIN_DIRECTORY = os.path.split(os.path.abspath(__file__))[0]

SCREEN_RECTANGLE = Rect(0, 0, DISPLAY_WIDTH, DISPLAY_HEIGHT)
SOUNDS_PATH = "data\\sounds"
