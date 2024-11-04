# декомпозиция проекта в отдельные файлы и директории
# From & import это инструменты для работы с модулями, директориями, классами и файлами

# import lesson1
# arzy = lesson1.Person("Арзы", 25, "Бишкек")
# arzy.introduce()
#
# from lesson1 import Person
# arzy = Person("Арзы", 25, "Бишкек")
# arzy.introduce()


# Принципы ООП
# Объектно-ориентированное программирование (ООП) — это парадигма программирования, которая основывается на
#    представлении программы как совокупности объектов, взаимодействующих между собой. Основные принципы ООП включают:

# Наследование: позволяет одному классу (производному) унаследовать свойства и методы другого класса (базового),
#    расширяя или изменяя их. Наследование способствует повторному использованию кода и созданию иерархии классов.

# Полиморфизм: предоставляет возможность объектам разных классов обрабатывать одно и то же сообщение по-разному.
#   С помощью полиморфизма можно создавать гибкие интерфейсы, работающие с разными типами объектов,
#    что повышает гибкость и масштабируемость кода.

# Инкапсуляция: предполагает объединение данных и методов, работающих с этими данными, в единое целое — объект.
#   Это позволяет скрыть внутреннее устройство объекта и защитить данные от прямого доступа и изменений извне.

# Абстракция: этот принцип позволяет выделить ключевые характеристики объектов, скрывая детали их реализации.
#    Благодаря абстракции, можно сосредоточиться на общих свойствах и поведении объектов, игнорируя излишние детали.

# Базовый\Супер\Родительский\
class Hero:
    def __init__(self, name, health):
        self.name = name
        self.health = health

    def introduce(self):
        return f"Я {self.name}, мой уровень здоровья: {self.health}"

    def rest(self):
        self.health += 10
        return f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.health}"

    def action(self):
        return f"{self.name} выполняет базовое действие.\n"

# Класс Mage, наследующийся от Hero
class Mage(Hero):
    def __init__(self, name, health, mana=100):
        super().__init__(name, health)
        self.mana = mana

    def cast_spell(self):
        if self.mana >= 10:
            self.mana -= 10
            return f"{self.name} использует заклинание! Оставшаяся мана: {self.mana}"
        else:
            return f"{self.name} недостаточно маны для заклинания!"

    def action(self):
        base_action = super().action()
        spell_result = self.cast_spell()  # Вызов метода внутри другого метода
        return f"{base_action} {spell_result}"

def hero_action(hero):
    print(hero.introduce())
    print(hero.rest())
    print(hero.action())

mage = Mage("Гэндальф", 100, 50)

hero_action(mage)

# # Класс Tank, наследующийся от Hero
# class Tank(Hero):
#     def __init__(self, name, health, armor):
#         super().__init__(name, health)
#         self.armor = armor
#
#     def action(self):
#         base_action = super().action()
#         return f"{base_action} {self.name} защищается мощным щитом! Броня: {self.armor}"
#
# Класс Healer, наследующийся от Hero
# class Healer(Hero):
#     def __init__(self, name, health, healing_power):
#         super().__init__(name, health)
#         self.healing_power = healing_power
#
#     def action(self):
#         base_action = super().action()
#         return f"{base_action} {self.name} исцеляет союзника целебным светом! Сила исцеления: {self.healing_power}"
#
# # Класс Warrior, наследующийся от Hero
# class Warrior(Hero):
#     def __init__(self, name, health, strength):
#         super().__init__(name, health)
#         self.strength = strength
#
#     def action(self):
#         base_action = super().action()
#         return f"{base_action} {self.name} атакует врага мощным ударом меча! Сила: {self.strength}"

# Пример использования метода super()


# Создание объектов разных классов
# mage = Mage("Гэндальф", 100, 50)
# tank = Tank("Артур", 150, 75)
# healer = Healer("Элена", 80, 40)
# warrior = Warrior("Тор", 120, 60)

# Полиморфное использование метода action и метода super()
# hero_action(mage)
# hero_action(tank)
# hero_action(healer)
# hero_action(warrior)

# gitignore

