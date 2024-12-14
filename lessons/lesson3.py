# # Инкапсуляция
#
# # Когда имя атрибута или метода начинается с одного подчеркивания (например, _balance),
# # это обозначает, что он защищен
# # или может начитаться с двух подчеркиваний (__balance), что обозначает, что он приват
#
#
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self._balance = balance  # Защищенный атрибут
#         self.__balance = balance  # Приватный атрибут
#
#     def deposit(self, amount):
#         if amount > 0:
#             self._balance += amount
#             return f"Баланс {self.owner} пополнен на {amount}. Текущий баланс: {self._balance}"
#         return "Сумма должна быть положительной."
#
#     def get_balance(self):
#         return f"Баланс: {self._balance}"
#
# # Использование защищенного атрибута
# account = BankAccount("Иван", 1000)
# print(account.get_balance())    # Баланс: 1000
# print(account._balance)      # Мы можем получить доступ к _balance, но это не рекомендуется.
#
#
#
# # Атрибуты или методы, начинающиеся с двойного подчеркивания (__balance),
# # считаются приватными.
#
# class BankAccount:
#     def __init__(self, owner, balance):
#         self.owner = owner
#         self.__balance = balance  # Приватный атрибут
#
#     def deposit(self, amount):
#         if amount > 0:
#             self.__balance += amount
#             return f"Баланс {self.owner} пополнен на {amount}. Текущий баланс: {self.__balance}"
#         return "Сумма должна быть положительной."
#
#     def get_balance(self):
#         return f"Баланс: {self.__balance}"
#
# # Пример использования приватного атрибута
# account = BankAccount("Иван", 1000)
# print(account.get_balance())  # Баланс: 1000
#
# # Прямой доступ к __balance вызовет ошибку, так как он скрыт
# print(account.__balance)      # Ошибка AttributeError: 'BankAccount' object has no attribute '__balance'
#
# # Подсказка: Просмотр всех атрибутов и методов объекта
# print(dir(account))
#
# # Доступ к приватному атрибуту через преобразованное имя
# print(account._BankAccount__balance)  # 1000
#
#
#
# # Абстракция позволяет сосредоточиться на общих характеристиках, скрывая детали
# # реализации. Это можно сделать, создавая абстрактные классы, которые определяют
# # интерфейс (методы) для классов-наследников. В Python абстрактные классы обычно
# # создаются с помощью модуля abc.
#
# from abc import ABC, abstractmethod
#
# class Animal(ABC):  # Абстрактный класс
#     @abstractmethod
#     def make_sound(self):
#         pass  # Определяет интерфейс для звука
#
#     @abstractmethod
#     def move(self):
#         pass  # Определяет интерфейс для движения
#
# class Dog(Animal):
#     def make_sound(self):
#         return "Гав-гав!"
#
#     def move(self):
#         return "Собака бегает на четырех лапах."
#
# class Bird(Animal):
#     def make_sound(self):
#         return "Чирик-чирик!"
#
#     def move(self):
#         return "Птица летит."
#
# # Пример использования абстракции
# dog = Dog()
# bird = Bird()
#
# print(dog.make_sound())  # Гав-гав!
# print(dog.move())        # Собака бегает на четырех лапах.
# print(bird.make_sound()) # Чирик-чирик!
# print(bird.move())       # Птица летит.
#
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
# class Animal:
#     def make_sound(self):
#         return "Издает звук"
#
# class Flyable:
#     def move(self):
#         return "Летит"
#
# class Swimmable:
#     def move(self):
#         return "Плавает"
#
# class Duck(Animal, Flyable, Swimmable):  # Множественное наследование
#     def make_sound(self):
#         return "Кря-кря!"
#
# # Пример использования множественного наследования
# duck = Duck()
# print(duck.make_sound())  # Кря-кря!
# print(duck.move())
#
# # Для просмотра порядка разрешения методов можно использовать атрибут __mro__ или функцию mro().
# # Порядок разрешения методов (MRO)
# print(Duck.__mro__)  # Массив классов в порядке их проверки для поиска методов


# Алмазная проблема (Diamond Problem):
# class A:
#     def speak(self):
#         print("Я класс A")
#
# class B(A):
#     def speak(self):
#         print("Я класс B")
#
# class C(A):
#     def speak(self):
#         print("Я класс C")
#
# class D(B, C):  # D наследует от B и C
#     pass
#
# d = D()
# d.speak()  # Какой метод будет вызван? Это зависит от порядка в MRO!

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















