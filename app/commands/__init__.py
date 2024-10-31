from abc import ABC, abstractmethod 
#contains defintion of the command classes to specific operations 

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
#shows the command defintion for an additioncommand 

    
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
            raise ZeroDivisionError("cannot divide by zero...try again!")
        return self.num1/self.num2 
    
