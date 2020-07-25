"""
- When naming classes we capitalize the first letter of every word 

- An object is an instance of a class

"""

# class Point:
#     def move(self):
#         print("move")
    
#     def draw(self):
#         print("draw")

# point1 = Point()
# point1.x = 10
# point1.y = 20

# print(point1.x)
# point1.draw()

""" We can make it cleaner by utilizing constructors """

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def move(self):
        print("move")
    
    def draw(self):
        print("draw")

point = Point(10, 20)
# point.x = 11
print(point.x)

""" Exercise """

# class Person:
#     def __init__(self, name):
#         self.name = name
    
#     def talk(self):
#         print(f"{self.name} says hello")

# Boy = Person("Bolu")
# girl = Person("Lindsay")
# Boy.talk()
# girl.talk()

""" Inheritance basics """

class Mammals:
    def walk(self):
        print("walk")

class Dogs(Mammals):
    def bark(self):
        print("bark bark")

class Cats(Mammals):
    pass

dog1= Dogs()

dog1.walk()
dog1.bark()