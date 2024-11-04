class Person:
    def __init__(self, name, age, city):
        self.name = name
        self.age = age
        self.city = city

    def introduce(self):
        print(f"Привет меня зовут {self.name}, мне {self.age} лет, я живу в {self.city}")

    def is_adult(self):
        if self.age >= 18:
            return True
        else:
            return False

    def __str__(self):
        return f"Имя: {self.name}\nВозраст: {self.age}\nГород: {self.city}"

person_one = Person("Алексей", 27, "Москва")
person_one.introduce()
person_one.is_adult()

person_two = Person("Олег", 17, "Санкт-Петербург")
person_two.introduce()
person_two.is_adult()

person_three = Person("Зузанна", 18, "Гданьск")
person_three.introduce()
person_three.is_adult()

print(person_three)