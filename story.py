from utils import print_with_delay_horizontal , clear_terminal



def start_game(character_name, loadGameData):
    user_name = input('\nWhat is the name you want to use in the game?\n==> ')
    confirm = input(f'\nAre you sure about using {user_name.upper()}?\nUse [confirm]  [not confirm]\n==> ').lower()

    if confirm == 'confirm':
        print(f'Ok, your name now is [{user_name.capitalize()}]\nLets go to the game!')
        main_character_name = user_name
        character_name.append(main_character_name)
        
        while True:
            clear_terminal()
            story_1(user_name)
            print('='*70)
            dialogue_bar = ['Auto', 'Skip', 'History', 'Settings']

            for footerBar in dialogue_bar:
                print(footerBar)
            user_input_choices = input('==> ').lower()

            if user_input_choices == 'settings':
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
                        break

def story_1(character_name):
    print('='*70)
    print_with_delay_horizontal('''Kamu terbangun di sebuah kamar, dengan keadaan matahari yang sudah bersinar.''')
    print('='*70)
    clear_terminal()
    print('='*70)
    print_with_delay_horizontal('Ketika kamu melihat jam, alangkah terkejutnya ketika jam sudah melewati angka 7')
    print('='*70)
    clear_terminal()
    print('='*70)
    print_with_delay_horizontal('Anda bergegas untuk berpakaian dan langsung menuju ke sekolah')
    print('='*70)
    clear_terminal()
    print('='*70)
    print_with_delay_horizontal(f'{character_name}: Aduh kenapa saya bisa telat bangun sih,')
    print('='*70)
    clear_terminal()
    print('='*70)
    print_with_delay_horizontal('dengan buru - buru ia langsung pergi ke sekolah dengan memakan makanan yang seadanya...')
    

