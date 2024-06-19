

import os
import time 
import sys

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

# Main Menu delay Displayed
def print_mainmenu_delay(text, delay = 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Text Delay per characters
def print_with_delay_horizontal(text, delay = 0.05):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()

# Set up for Better Cleaned text
def space_align(text):
    print('='*70)
    print_with_delay_horizontal(text)
    print('='*70)
    clear_terminal()

# Text without deletion, for better clean text
def space_align_without_deleted_text(text):
    print('='*70)
    print_with_delay_horizontal(text)


def dialogue_delay(text, delay=0.1, pause=1):
    print_with_delay_horizontal(text, delay)
    time.sleep(pause)
    clear_terminal()

def delay_time_screen(text, delay=0.1, pause=4):
    clear_terminal()
    print_with_delay_horizontal(text, delay)
    time.sleep(pause)
    clear_terminal()