from pi_dec import pi_digits
from display import animated_stream
import itertools

def main():
    gen = pi_digits()
    print("π = ", end='', flush=True)  # первая часть

    mode = input("Введите количество цифр или 'inf' для бесконечного потока: ").strip()
    sound_mode = input("Включить мелодию? (y/n): ").strip().lower() == 'y'
    delay = input("Введите задержку между цифрами (секунды, например 0.02): ").strip()
    try:
        delay = float(delay)
    except:
        delay = 0.02  # стандартная задержка

    try:
        if mode.lower() == 'inf':
            # бесконечный поток
            animated_stream(gen, sound=sound_mode, delay=delay)
        else:
            # фиксированное количество цифр
            try:
                num = int(mode)
            except ValueError:
                print("Неверное число, запускаем бесконечный поток")
                animated_stream(gen, sound=sound_mode, delay=delay)
                return

            # берём ровно num цифр
            animated_stream(itertools.islice(gen, num), sound=sound_mode, delay=delay)

    except KeyboardInterrupt:
        print("\nВыход по Ctrl+C")

if __name__ == "__main__":
    main()
