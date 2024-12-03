
class Animal:
    def __init__(self, name):
        self.name = name

    def speak(self):
        print("I am an animal")


class Dog(Animal):
    def speak(self):
        return "Woof"


class Cat(Animal):
    def speak(self):
        return "Meow"



dog = Dog("Buddy")
dog.speak()

cat = Cat("Kitty")
cat.speak()

print(dog.name, dog.speak())
print(cat.name, cat.speak())