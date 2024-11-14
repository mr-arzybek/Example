# Тема урока Пакеты, модули, библиотеки и Фреймворки
# venv , pip
from colorama import init, Fore, Back, Style

# Инициализация (необходима для Windows)
init()

# Используем Fore для текста разных цветов
print(Fore.RED + 'Этот текст красный')
print(Fore.GREEN + 'Этот текст зеленый')
print(Fore.BLUE + 'Этот текст синий')

# Используем Back для фона разных цветов
print(Back.YELLOW + 'Текст с желтым фоном' + Back.RESET)

# Используем Style для обнуления стиля
print(Style.RESET_ALL + 'Текст со стандартными цветами')
