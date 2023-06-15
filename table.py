"""table object for Fifteens game. Always an ellipse, always brown"""

import pygame

# table class
class Table:

    def __init__(self):
        """table class that is a brown ellipse onscreen"""

        # attributes
        self.x_offset = 250
        self.y_offset = 300
        self.width = 300
        self.height = 100
        self.center_x = self.x_offset + (self.width // 2)
        self.center_y = self.y_offset + (self.height // 2)
        self.table_color = (205,133,63) # brown


    def draw_table(self, screen):
        """function to draw the table object when called"""
        # draw the object onscreen
        pygame.draw.ellipse(screen, self.table_color, 
                            (self.x_offset, 
                             self.y_offset, 
                             self.width, 
                             self.height), 
                             width= 0)

