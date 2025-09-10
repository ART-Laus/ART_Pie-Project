from colorama import Fore, Style, init
import random
import platform
import time
import shutil

init(autoreset=True)

COLORS = [Fore.RED, Fore.GREEN, Fore.YELLOW, Fore.CYAN, Fore.MAGENTA, Fore.BLUE, Fore.WHITE]

BASE_FREQ = 220  # минимальная частота (A3)
NOTE_DURATIONS = [50, 80, 120, 160]  # длительность нот

def colored_digit(digit):
    color = random.choice(COLORS)
    return f"{color}{digit}{Style.RESET_ALL}"

def play_note(digit, accent=False):
    """Проигрывает нотку для цифры, акцент — длиннее."""
    try:
        freq = BASE_FREQ + int(digit) * 40
        duration = NOTE_DURATIONS[int(digit) % len(NOTE_DURATIONS)]
        if accent:
            duration = int(duration * 1.5)
        if platform.system() == "Windows":
            import winsound
            winsound.Beep(freq, duration)
        else:
            time.sleep(duration / 1000)
    except Exception:
        pass

def animated_stream(gen, sound=False, delay=0.02):
    """Выводит цифры π с плавной анимацией в одну строку, с π = в начале."""
    try:
        width = shutil.get_terminal_size().columns
    except:
        width = 80

    count = 0
    first = True  # чтобы добавить π = перед первой цифрой

    for d in gen:
        if first:
            print("π = ", end='', flush=True)
            first = False

        print(colored_digit(d), end='', flush=True)

        if sound:
            accent = (count % 10 == 0)
            play_note(d, accent=accent)

        count += 1
        if count % (width - 4 if first else width) == 0:  # учитываем длину π =
            print()
        time.sleep(delay)
