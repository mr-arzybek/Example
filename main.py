# from abc import ABC, abstractmethod
#
# class Room(ABC):
#     def __init__(self, features, price):
#         self._features = features
#         self.__price = price
#
#     @abstractmethod
#     def get_price(self):
#         pass
#
#     @abstractmethod
#     def get_features(self):
#         pass
#
#
# class StandardRoom(Room):
#     def __init__(self, features, price):
#         super().__init__(features, price)
#
#     def get_price(self):
#         return self._Room__price
#
#     def get_features(self):
#         return self._features
#
#
# class LuxuryRoom(Room):
#     def __init__(self, features, price):
#         super().__init__(features, price)
#
#     def get_price(self):
#         return self._Room__price
#
#     def get_features(self):
#         return self._features
#
#
# class FamilyRoom(Room):
#     def __init__(self, features, price):
#         super().__init__(features, price)
#
#     def get_price(self):
#         return self._Room__price
#
#     def get_features(self):
#         return self._features
#
#
# class WiFiService:
#     def get_wifi_description(self):
#         return "Быстрый Wi-Fi по всему отелю."
#
#
# class BreakfastService:
#     def get_breakfast_description(self):
#         return "Шведский стол только со свежими продуктами."
#
#
# class LuxuryRoomWithServices(LuxuryRoom, WiFiService, BreakfastService):
#     def __init__(self, features, price):
#         LuxuryRoom.__init__(self, features, price)
#         WiFiService.__init__(self)
#         BreakfastService.__init__(self)
#
#     def get_features(self):
#         features = super().get_features()
#         features.append(self.get_wifi_description())
#         features.append(self.get_breakfast_description())
#         return features
#
#
# class FamilyRoomWithWiFi(FamilyRoom, WiFiService):
#     def __init__(self, features, price):
#         FamilyRoom.__init__(self, features, price)
#         WiFiService.__init__(self)
#
#     def get_features(self):
#         features = super().get_features()
#         features.append(self.get_wifi_description())
#         return features
#
#
# def print_room_info(room):
#     print(f"Цена: {room.get_price()}$")
#     print("Удобства:")
#     for feature in room.get_features():
#         print(f"- {feature}")
#     print(
#
#     )
#
#
# wifi_service = WiFiService()
# breakfast_service = BreakfastService()
#
# standard_room = StandardRoom(features=["Кровать", "Телевизор", "Мини-бар"], price=100)
# luxury_room = LuxuryRoom(features=["Кровать King-size", "Телевизор 4K", "Спа-ванна", "Мини-бар"], price=200)
# family_room = FamilyRoom(features=["Кровать King-size", "Две кровати", "Детская зона", "Телевизор"], price=125)
# luxury_room_with_services = LuxuryRoomWithServices(features=["Кровать King-size", "Телевизор 4K", "Спа-ванна", "Мини-бар"], price=250)
# family_room_with_services = FamilyRoomWithWiFi(features=["Кровать King-size", "Две кровати", "Детская зона", "Телевизор"], price=150)
#
# print_room_info(standard_room)
# print_room_info(luxury_room)
# print_room_info(family_room)
# print_room_info(luxury_room_with_services)
# print_room_info(family_room_with_services)

from abc import ABC, abstractmethod
import random

class Hero:

    def __init__(self, name, hp, lvl):
        self.name = name
        self.hp = hp
        self.lvl = lvl
        self._luck = random.randint(0, 100)
        self.__crit_dmg = random.randint(0, 100)

    def __heal_hp(self):
        return random.randint(0, 100)

    def greetings(self):
        return print(f"Привет, {self.name}!\n Мой уровень: {self.lvl}")

    def status(self):
        return print(f"LVL: {self.lvl} \nHP: {self.hp}" )

    def attack(self):
        if self.__crit_dmg >= 30:
            return print(f"{self.name} критический удар!")
        else:
            return print(f"{self.name} базовый удар!")

    def protection(self):
        if self._luck >= 20:
            return print(f"{self.name} успешно защищается!")
        else:
            return print(f"{self.name} не смог защититься!")

    def rest(self):
        self.hp += self.__heal_hp()
        return print(f"{self.name} отдыхает и восстанавливает здоровье. Новое здоровье: {self.hp}")

    # @abstractmethod
    # def unique_attack(self):
    #     pass
    #
    # @abstractmethod
    # def unique_scream(self):
    #     pass

test = Hero("test", 100, 1)

print(test._luck)
print(dir(test))
print(test._Hero__crit_dmg)


class ShieldHero(Hero):

    def __init__(self, name, hp, lvl, aura=0):
        super().__init__(name, hp, lvl)
        self.aura = aura

    def protection(self):
        if self._luck >= 20:
            return print(f"{self.name} успешно защищается!")
        else:
            self.aura += 100
            return print(f"{self.name} не смог защититься!")

    def unique_attack(self):
        if self.aura >= 10:
            return print(f"{self.name} выполняет уникальную атаку!")

    def unique_scream(self):
        return print(f"{self.name} выполняет уникальный крик Бла бла бла!")


naofumi = ShieldHero("naofumi", 100, 1)



# 3. Множественное наследование

# Множественное наследование позволяет классу наследовать поведение и свойства сразу от нескольких классов.
# Однако это может привести к путанице, особенно если в классах есть методы с одинаковыми именами.
# # Python решает такие проблемы с помощью механизма порядка разрешения методов (Method Resolution Order, MRO),
# # который определяет, какой метод или атрибут будет вызван в случае конфликтов.
#
# # Как работает множественное наследование в Python
# # Наследование нескольких классов: Один класс может наследовать несколько классов, что дает ему доступ
# # ко всем методам и атрибутам этих классов.
# # Метод разрешения порядка (MRO): Python использует алгоритм C3-линеаризации для определения порядка,
# # в котором методы классов будут вызваны, если они определены в нескольких родительских классах.
# # Конфликты методов: Если в разных родительских классах есть методы с одинаковыми именами,
# # Python будет искать их в порядке, определенном MRO.

# Животные
class Animal:
    def make_sound(self):
        return "Издает звук"
# Летающие
class Flyable:
    def move(self):
        return "Летит"
# Плавающие
class Swimmable:
    def move(self):
        return "Плавает"
# Утка
class Duck(Animal, Flyable, Swimmable):  # Множественное наследование
    def make_sound(self):
        return "Кря-кря!"

# Пример использования множественного наследования
duck = Duck()
print(duck.make_sound())  # Кря-кря!
print(duck.move())  # Летит

# # # Для просмотра порядка разрешения методов можно использовать атрибут __mro__ или функцию mro().
# # # Порядок разрешения методов (MRO)
print(Duck.__mro__)  # Массив классов в порядке их проверки для поиска методов



# # Подводные камни:
# # Ошибка при создании экземпляров абстрактных классов: Нельзя создать экземпляр абстрактного класса Animal,
# # иначе Python выбросит ошибку, поскольку в нём есть неопределённые абстрактные методы.
# #
# # Обязательное определение всех абстрактных методов в подклассах:
# # Каждый класс-наследник должен реализовать все абстрактные методы, иначе он тоже станет абстрактным.
#
#
#
#     # 3. Множественное наследование
#
#     # Множественное наследование позволяет классу наследовать поведение и свойства сразу от нескольких классов.
#     # Однако это может привести к путанице, особенно если в классах есть методы с одинаковыми именами.
# # Python решает такие проблемы с помощью механизма порядка разрешения методов (Method Resolution Order, MRO),
# # который определяет, какой метод или атрибут будет вызван в случае конфликтов.
#
# # Как работает множественное наследование в Python
# # Наследование нескольких классов: Один класс может наследовать несколько классов, что дает ему доступ
# # ко всем методам и атрибутам этих классов.
# # Метод разрешения порядка (MRO): Python использует алгоритм C3-линеаризации для определения порядка,
# # в котором методы классов будут вызваны, если они определены в нескольких родительских классах.
# # Конфликты методов: Если в разных родительских классах есть методы с одинаковыми именами,
# # Python будет искать их в порядке, определенном MRO.
#
class Animal:
    def make_sound(self):
        return "Издает звук"

class Flyable:
    def move(self):
        return "Летит"

class Swimmable:
    def move(self):
        return "Плавает"

class Duck(Animal, Flyable, Swimmable):  # Множественное наследование
    def make_sound(self):
        return "Кря-кря!"
#
# # Пример использования множественного наследования
duck = Duck()
print(duck.make_sound())  # Кря-кря!
print(duck.move())
#
# # Для просмотра порядка разрешения методов можно использовать атрибут __mro__ или функцию mro().
# # Порядок разрешения методов (MRO)
# print(Duck.__mro__)  # Массив классов в порядке их проверки для поиска методов


# Алмазная проблема (Diamond Problem):
class A:
    def speak(self):
        print("Я класс A")

class B(A):
    def speak(self):
        print("Я класс B")

class C(A):
    def speak(self):
        print("Я класс C")

class D(B, C):  # D наследует от B и C
    pass


d = D()
d.speak()  # Какой метод будет вызван? Это зависит от порядка в MRO!

# class A:
#     def speak(self):
#         print("Я класс A")
#
# class B(A):
#     def speak(self):
#         super().speak()  # Вызываем speak из класса A
#         print("Я класс B")
#
# class C(A):
#     def speak(self):
#         super().speak()  # Вызываем speak из класса A
#         print("Я класс C")
#
# class D(B, C):
#     def speak(self):
#         super().speak()  # Вызов super() от B и C
#         print("Я класс D")
#
# d = D()
# d.speak()

# class A:
#     def greet(self):
#         print("Hello from A")
#
# class B(A):
#     def greet(self):
#         print("Hello from B")
#
# class C(A):
#     def greet(self):
#         super().greet()
#         print("Hello from C")
#
# class D(B, C):
#     def greet(self):
#         super().greet()
#         print("Hello from D")
#
# d = D()
# d.greet()

# Создание атрибута на лету
# class MyClass:
#     pass
#
# obj = MyClass()
# obj.new_attr = "Dynamic"  # Создание атрибута на лету
# print(obj.new_attr)


# Использовать __slots__, если хотите ограничить набор атрибутов.
# Если вы хотите ограничить доступ к атрибутам и методам,
# используйте __slots__ в качестве метакласса.
# class MyClass:
#     __slots__ = ["name", "age"]
#
# obj = MyClass()
# obj.name = "John"
# obj.age = 30
# obj.height = 180
# print(obj.name)  # John
# print(obj.age)  # 30
# print(obj.height)

# Неожиданное поведение мутабельных атрибутов
# class MyClass:
#     shared_list = []
#
# obj1 = MyClass()
# obj2 = MyClass()
# obj1.shared_list.append(1)
# print(obj2.shared_list)  # [1]
#
# # решение мутабельных атрибутов
# class MyClass:
#     def __init__(self):
#         self.shared_list = []

