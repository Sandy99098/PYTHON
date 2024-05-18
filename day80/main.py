# Your Python code goes here
# MULTILEVEL INHERITANCE
class Animal:
    def __init__(self, animalType) -> None:
        self.animalType = animalType

    def show(self):
        print(f"Type of animal class is {self.animalType}")

class Terrestrial(Animal):
    def __init__(self, animalType, animalLive) -> None:
        super().__init__(animalType)
        self.animalLive = animalLive

    def show(self):
        print(f"This animal is a {self.animalType} that lives on {self.animalLive}")

class Dog(Terrestrial):
    def __init__(self, name, animalType, animalLive):
        super().__init__(animalType, animalLive)
        self.name = name

    def show(self):
        print(f"Dog name is {self.name}, which is a {self.animalType} and lives on {self.animalLive}")

# Creating an instance of Dog
d = Dog("Golden Retriever", "Dog", "land")
d.show()

# Creating an instance of Terrestrial
t = Terrestrial("Land animal", "land")
t.show()
