class Person:
    def __init__(self, name):
        self.name= name
    def greet(self):
        return f"Hello, my name is {self.name}."
    def __str__(self):
        return self.name
    
