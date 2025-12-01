class Person:
    def print(self):
        print("Name: ", self.name)
        print("Age: ", self.age)
        
    def __init__(self, n, a):
        self.name = n
        self.age = a
        
    def __lt__(self, other):
        return self.age < other.age
    
    def __str__(self):
        return f"My name is {self.name}. Age: {self.age}"
    
class President(Person):
    def set_term(self, term):
        print(f"Setting to {term}")
        self.term = term 

macron = President("Emm", 47)
print(macron)