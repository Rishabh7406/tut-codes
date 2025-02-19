#rutnime poly
class Animal:
    def make_sound(self):
        return "Some sound"

class Dog(Animal):
    def make_sound(self):
        return "Bark"

class Cat(Animal):
    def make_sound(self):
        return "Meow"

# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.make_sound())  # Output: Bark, Meow
