from utils import clear_terminal, delay_time_screen
from storyline import story_Act_1, Story_prolog



def start_game(character_name, loadGameData):
    user_name = input('\nWhat is the name you want to use in the game?\n==> ')
    confirm = input(f'\nAre you sure about using {user_name.upper()}?\nUse [confirm]  [not confirm]\n==> ').lower()

    if confirm == 'confirm':
        print(f'Ok, your name now is [{user_name.capitalize()}]\nLets go to the game!')
        main_character_name = user_name
        character_name.append(main_character_name)
        
        while True:
            delay_time_screen('Now loading...')
            Story_prolog(user_name)
            story_Act_1(user_name)
            print('='*70)
            dialogue_bar = ['Auto', 'Skip', 'History', 'Settings']

            for footerBar in dialogue_bar:
                print(footerBar)

            user_input_choices = input('==> ').lower()


            if user_input_choices == 'settings':
                from menu import submenu_settings
            submenu_settings()
            break







