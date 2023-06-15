import pytest
from player import Player, MasterPlayer
from table import Table
# import main
# from main import *

# checks if player and table spawn in 
# correct place, and have correct colors
# using assert

def test_player_creation():
    """test that player is created right"""
    player = Player(0, 0, (255, 0, 0))
    assert player.x_coord == 0
    assert player.y_coord == 0
    assert player.color == (255, 0, 0)

def test_master_creation():
    """test that master player is right"""
    master_player = MasterPlayer(0, 0, (0, 255, 0))
    assert master_player.x_coord == -30
    assert master_player.y_coord == 0
    assert master_player.color == (0, 255, 0)

def test_table_creation():
    """test that table is right"""
    table = Table()
    assert table.x_offset == 250
    assert table.y_offset == 300
    assert table.width == 300
    assert table.height == 100
    assert table.center_x == 400
    assert table.center_y == 350
    assert table.table_color == (205, 133, 63)

# def test_text_creation():
#     text_now = main.input_font.render(text_input, True, (0, 0, 0))
#     pass

# def test_game_muzak():
#     pass

# def test_add_points():
#     pass

# def test_collision():
#     pass
