from abc import ABC, abstractmethod 

class Command(ABC):
    @abstractmethod 
    def execute(self):
        pass 

class AddCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        return self.num1 + self.num2 
    
    
class SubtractCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        return self.num1 - self.num2 
    
    
class MultiplyCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        return self.num1 * self.num2 
    
    
class DivideCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        if self.num2 == 0 :
            raise ValueError("Cannot divide by zero. Try again.")
        return self.num1/self.num2 
    

class GreetCommand():
    def __init__(self)
        