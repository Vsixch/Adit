import time as t
import sys as s
from story import start_game
from utils import clear_terminal , print_with_delay_horizontal, print_mainmenu_delay, delay_time_screen

loadGameData = []
character_name = []

def main_menu(character_name, loadGameData):
    
     while True:
        clear_terminal()
        print('-- The Mystery Of Everdawn! --')
        options = [
                   '\n- Start Game', 
                   '\n- Load Game', 
                   '\n- Settings', 
                   '\n- Credits', 
                   '\n- Exit Game']
        
        for option in options:
            print_mainmenu_delay(option)

        
        user_input = input('\n==> ').lower().replace(' ', '')

        if user_input == 'startgame':
            delay_time_screen('loading... please wait...')
            start_game(character_name, loadGameData)
        elif user_input == 'loadgame':
            load_game(loadGameData)
        elif user_input == 'exitgame':
            exit_game(character_name)
            break

def load_game(loadGameData):
    if not loadGameData:
        print('='*20,'\n','No data has been save!','\n','='*20)
    else:
        print('This is your data game,')
        for data in loadGameData:
            print(data)

def exit_game(character_name):
    for name in character_name:
        print_with_delay_horizontal(f'See you next time, {name}')

def submenu_settings():
 
    menu_in_game = ['\n-- Menu --\n', 
                    '\n- Load Game', 
                    '\n- Settings', 
                    '\n- Credits', 
                    '\n- Return to Main Menu\n']
        
    for MenuGame in menu_in_game:
            print(MenuGame)

    user_input_menu = input('==> ').lower().replace(' ', '')

    if user_input_menu == 'returntomainmenu':
        print('Are you sure you want to go back to the Main Menu?\nUse [confirm]  [not confirm]')    
        confirm = input('==> ').lower()
        if confirm == 'confirm':
            print('\n')
            return


 


