from colorama import Fore, Style, init
import random
import platform
import time
import shutil
import sys

init(autoreset=True)

COLORS = [
    Fore.RED, Fore.GREEN, Fore.YELLOW,
    Fore.CYAN, Fore.MAGENTA, Fore.BLUE, Fore.WHITE
]

BASE_FREQ = 220  # минимальная частота (A3)
NOTE_DURATIONS = [50, 80, 120, 160]  # длительности нот в мс


def colored_digit(digit, bright=False):
    """Возвращает цифру с цветом (яркую или обычную)."""
    color = random.choice(COLORS)
    style = Style.BRIGHT if bright else Style.NORMAL
    return f"{style}{color}{digit}{Style.RESET_ALL}"


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
    """
    Выводит цифры π с анимацией:
    - плавный поток
    - цвет
    - мерцание (яркое появление → нормальное состояние)
    - опциональный звук
    """
    try:
        width = shutil.get_terminal_size().columns
    except Exception:
        width = 80

    count = 0
    first = True  # чтобы добавить "π = " перед первой цифрой

    for d in gen:
        if first:
            sys.stdout.write("π = ")
            sys.stdout.flush()
            first = False

        # сначала яркая версия цифры
        sys.stdout.write(colored_digit(d, bright=True))
        sys.stdout.flush()
        time.sleep(delay / 2)

        # затем сразу тусклая версия поверх
        sys.stdout.write(f"\b{colored_digit(d, bright=False)}")
        sys.stdout.flush()

        if sound:
            accent = (count % 10 == 0)
            play_note(d, accent=accent)

        count += 1
        if count % width == 0:
            sys.stdout.write("\n")
            sys.stdout.flush()

        time.sleep(delay / 2)
