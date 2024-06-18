import sys
import time

def print_with_delay_horizontal(text, delay=0.1):
    for char in text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print()  # Untuk mengakhiri baris setelah selesai mencetak

# Contoh penggunaan
print_with_delay_horizontal("Hello, this is delayed printing horizontally.")