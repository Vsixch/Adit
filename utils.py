import os
import time 
import sys

def clear_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def print_with_delay_horizontal(text, delay = 0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()