class Parent:
    def prt_method(self, name, age):
        self.name = name
        self.age = age
        print(f"Parent method called with name: {self.name} and age: {self.age}")

class Child(Parent):
    def prt_method(self, name, age):
        print("This is  inside child method")
        super().prt_method(name, age)  # Calling the parent class's method

    @classmethod
    def info(cls , string):
        name, age = string.split("-")
        cls.name = name
        cls.age = int(age)
        # cls.string= string.split("-")[0] , string.split("-")[1]
        # print(f"Name is {cls.string[0]} and age is {cls.string[1]}")
        print(f"Name is {cls.name} and age is {cls.age}")
        # print(type(cls.age))

# Creating an instance of Parent and calling prt_method
a = Parent()
a.prt_method("hello", 67)

# Creating an instance of Child and calling prt_method and info
c = Child()
c.prt_method("Sandy", 21)

string = "Sandy-21"
c.info(string)
