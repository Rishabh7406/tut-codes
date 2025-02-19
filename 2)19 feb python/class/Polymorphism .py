class Animal:
    def sound(self):
        pass  # Abstract method

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"

# Polymorphism in action
animals = [Dog(), Cat()]
for animal in animals:
    print(animal.sound())  # Output: Bark, Meow
