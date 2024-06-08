# Introduction and properties of inheritance in Python

# Base class
class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        return "Some generic animal sound"

    def info(self):
        return f"I am an animal named {self.name}."

# Single inheritance (Bird inherits from Animal)
class Bird(Animal):
    def __init__(self, name, can_fly):
        super().__init__(name)
        self.can_fly = can_fly

    def sound(self):
        return "Chirp chirp"

    def info(self):
        parent_info = super().info()
        fly_info = "can fly" if self.can_fly else "cannot fly"
        return f"{parent_info} I am a bird and I {fly_info}."

# Multiple inheritance (Sparrow inherits from Bird and another base class)
class Color:
    def __init__(self, color):
        self.color = color

    def info(self):
        return f"My color is {self.color}."

class Sparrow(Bird, Color):
    def __init__(self, name, can_fly, color):
        Bird.__init__(self, name, can_fly)
        Color.__init__(self, color)

    def info(self):
        bird_info = Bird.info(self)
        color_info = Color.info(self)
        return f"{bird_info} {color_info}"

print(Sparrow.mro())
animal = Animal("Generic Animal")
bird = Bird("Parrot", True)
sparrow = Sparrow("Jack", True, "brown")
print(animal.sound())    
print(animal.info())     

print(bird.sound())      
print(bird.info())       

print(sparrow.sound())   
print(sparrow.info())    