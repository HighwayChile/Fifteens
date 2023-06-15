
import pygame
from pygame.locals import *
import random
from player import *
from table import Table

pygame.init()

game_list = ["1", "2", "3", "4", "5", 
             "6", "7", "8", "9", "10", 
             "11", "12", "13", "14", "15", 
             "LOSE A POINT FOR CLICKING HELP"]

counter_index = 0
text_input = ""
selected_index = None
points = 0
point_counted = False
music_stopped = False

screen_width = 800
screen_height = 600
screen_color = (0, 45, 0)

screen = pygame.display.set_mode((screen_width, screen_height))
clock = pygame.time.Clock()
pygame.display.set_caption("Fifteens")

input_font = pygame.font.Font(None, 48)
number_font = pygame.font.Font(None, 30)
button_font = pygame.font.Font(None, 24)

table = Table()

players = []

Charles = Player((table.center_x - 190), (table.center_y - 50), (255, 0, 0))
Timothy = Player((table.center_x - 90), (table.center_y - 90), (0, 150, 0))
Frank = Player((table.center_x + 40), (table.center_y - 90), (255, 255, 0))
Rudiger = Player((table.center_x + 140), (table.center_y - 50), (0, 0, 255))
Dickie = MasterPlayer((table.center_x - 42), (table.center_y + 220), (0, 0, 0))

players.append(Charles) 
players.append(Timothy) 
players.append(Frank) 
players.append(Rudiger) 
players.append(Dickie)

def choose_random_word():

    with open("word_list.txt", "r") as file:
        lines = file.readlines()
    random_line = random.choice(lines)
    random_word = random_line.strip()
    return random_word

def display_number_above_player(player_index, number):

    player = players[player_index]
    number_text = input_font.render(str(number), True, (0, 0, 0))
    number_text_rect = number_text.get_rect()
    number_text_rect.topleft = (player.x_coord + player.width // 2 
                                - number_text_rect.width // 2, 
                                player.y_coord - number_text_rect.height - 5)
    screen.blit(number_text, number_text_rect)

def play_music():
    pygame.mixer.music.load("Fifteens.mp3")
    pygame.mixer.music.play(loops= -1)

def stop_music():
    pygame.mixer.music.stop()

play_music()

running = True
while running:

    if points > 14:
        screen.fill(screen_color)
        win_surface = input_font.render("YOU FRIGGIN' WON, PAL!", True, (0, 0, 0))
        win_rect = win_surface.get_rect(center=(screen_width // 2, 150))
        screen.blit(win_surface, win_rect)
        pygame.display.update()
    else:
        screen.fill(screen_color)

    title_surface = input_font.render("Fifteens", True, (0, 0, 0))
    title_rect = title_surface.get_rect(center=(screen_width // 2, 50))
    screen.blit(title_surface, title_rect)

    for i, player in enumerate(players):
        player.draw_player(screen)

        if counter_index < 15:
            if counter_index % len(players) == i:
                display_number_above_player(i, counter_index + 1)

    for i, index in enumerate(game_list):
        x = (i % 15) * 40 + 80 
        y = (i // 15) * 100 + 500
        pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(x, y, 10, 10))

    table.draw_table(screen)

    accept_button_rect = pygame.Rect(360, 400, 80, 30)
    accept_button_font = button_font
    accept_button_text = accept_button_font.render("Accept", True, (0, 0, 0))
    accept_button_text_rect = accept_button_text.get_rect(
        center=accept_button_rect.center)
    button_color = (150, 150, 150)
    pygame.draw.rect(screen, button_color, accept_button_rect)
    screen.blit(accept_button_text, accept_button_text_rect)

    random_button_rect = pygame.Rect(460, 400, 80, 30)
    random_button_font = button_font
    random_button_text = random_button_font.render("Random", True, (0, 0, 0))
    random_button_text_rect = random_button_text.get_rect(
        center=random_button_rect.center)
    button_color = (150, 150, 150)
    pygame.draw.rect(screen, button_color, random_button_rect)
    screen.blit(random_button_text, random_button_text_rect)

    help_button_rect = pygame.Rect(260, 400, 80, 30)
    help_button_font = button_font
    help_button_text = help_button_font.render("Help", True, (0, 0, 0))
    help_button_text_rect = help_button_text.get_rect(
        center=help_button_rect.center)
    button_color = (150, 150, 150)
    pygame.draw.rect(screen, button_color, help_button_rect)
    screen.blit(help_button_text, help_button_text_rect)

    sound_button_rect = pygame.Rect(700, 550, 80, 30)
    sound_button_font = button_font
    sound_button_text = sound_button_font.render("sound", True, (0, 0, 0))
    sound_button_text_rect = sound_button_text.get_rect(
        center=sound_button_rect.center)
    button_color = (150, 150, 150)
    pygame.draw.rect(screen, button_color, sound_button_rect)
    screen.blit(sound_button_text, sound_button_text_rect)
    
    input_text = input_font.render(text_input, True, (0, 0, 0))
    input_text_rect = input_text.get_rect(center=(screen_width // 2, 340))
    screen.blit(input_text, input_text_rect)

    if counter_index == 15 and not point_counted:
        points += 1
        point_counted = True
    if counter_index < len(game_list) - 1:
        notice_surface = input_font.render(
            f"Type out the value at index "
            f"{counter_index + 1}", True, (0, 0, 0))
        notice_rect = notice_surface.get_rect(center=((screen_width // 2), 
                                                      100))
        screen.blit(notice_surface, notice_rect)
    elif counter_index == len(game_list) - 1 and selected_index is not None:
        notice_surface = input_font.render("Choose a word, fella", True, 
                                           (0, 0, 0))
        notice_rect = notice_surface.get_rect(center=((screen_width // 2), 
                                                      100))
        screen.blit(notice_surface, notice_rect)
    elif counter_index == len(game_list) - 1:
        notice_surface = input_font.render(f"Choose a number twixt 1-15", 
                                           True, (0, 0, 0))
        screen.blit(notice_surface, notice_rect)

    if selected_index is not None:
        selected_text = number_font.render(f"Selected: {selected_index + 1}", True, (0, 0, 0)) 
        selected_text_rect = selected_text.get_rect(center=(screen_width // 2, 370))
        screen.blit(selected_text, selected_text_rect)


        for i, index in enumerate(game_list):
            x = (i % 15) * 40 + 80
            y = (i // 15) * 100 + 500
            rect_color = (0, 0, 0)
            if i == selected_index:
                rect_color = (200, 200, 0)
            pygame.draw.rect(screen, rect_color, pygame.Rect(x, y, 10, 10))
    
    points_text = number_font.render(f"Points: {points}", True, (0, 0, 0))
    points_text_rect = points_text.get_rect(topleft=(25, 25))
    screen.blit(points_text, points_text_rect)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if accept_button_rect.collidepoint(event.pos):

                if counter_index < len(game_list) - 1 \
                    and selected_index is None:
                    if text_input == game_list[counter_index]:
                        counter_index += 1
                        text_input = ""

                elif counter_index == len(game_list) - 1 \
                    and selected_index is None:
                    text_input = ""
                
                elif selected_index is not None:
                    if text_input != "":
                        game_list[selected_index] = text_input
                        text_input = ""
                        selected_index = None
                        counter_index = 0
            
            elif help_button_rect.collidepoint(event.pos):
                current_number = game_list[counter_index]
                number_text = input_font.render(f"{current_number}", True, 
                                                (255, 255, 255))
                number_text_rect = number_text.get_rect(center=(screen_width 
                                                                // 2, 200))
                screen.blit(number_text, number_text_rect)
                print(f"the word at {counter_index+1} is '{current_number}'")
                points -= 1
            
            elif random_button_rect.collidepoint(event.pos):
                text_input = choose_random_word()

            elif sound_button_rect.collidepoint(event.pos) \
                and music_stopped == True:
                play_music()
                music_stopped = False
            elif sound_button_rect.collidepoint(event.pos) \
                and music_stopped == False:
                stop_music()
                music_stopped = True

        elif event.type == pygame.KEYDOWN:
            if counter_index < len(game_list) - 1 and selected_index is None:
                if event.key == pygame.K_RETURN:
                    if text_input == game_list[counter_index]:
                        counter_index += 1
                        selected_index = None
                        text_input = ""
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

            elif counter_index == len(game_list) - 1 \
                and selected_index is None:
                if event.key == pygame.K_RETURN:
                    try:
                        if 0 < int(text_input) <= 15:               
                            if text_input != "":
                                selected_index = int(text_input) - 1
                                text_input = ""
                        else:
                            print("only numbers twixt 1-15")
                    except ValueError:
                        print("ONLY NUMBERS WORK")

                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

            elif selected_index is not None:
                if event.key == pygame.K_RETURN:
                    if text_input != "":
                        game_list[selected_index] = text_input
                        text_input = ""
                        selected_index = None
                        counter_index = 0
                        point_counted = False
                elif event.key == pygame.K_BACKSPACE:
                    text_input = text_input[:-1]
                else:
                    text_input += event.unicode

    pygame.display.update()
    clock.tick(30)

pygame.quit()
