"""Player class for a word game called fifteens. One subclass

Richard Sapp
13 June, 2023

"""

import pygame


class Player:
    def __init__(self, x_coord, y_coord, color):
        """parent class"""

        # attributes
        self.width = 50
        self.height = 80
        self.x_coord = x_coord
        self.y_coord = y_coord
        self.color = color

    # draw the player onscreen if called
    def draw_player(self, screen):
        """function to draw the player(s)"""
        pygame.draw.rect(screen, self.color, pygame.Rect(self.x_coord, 
                                                         self.y_coord, 
                                                         self.width, 
                                                         self.height))

# child class of player
class MasterPlayer(Player):
    def __init__(self, x_coord, y_coord, color):
        """This is a child class that was intended to be player1 in 
        a multiplayer game. Inherits from parent.

        """
        # attributes
        self.name = ""
        self.width = 150
        self.height = 80
        self.x_coord = x_coord - 30
        self.y_coord = y_coord
        self.color = color

