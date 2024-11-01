from abc import ABC, abstractmethod 
import logging 
import logging.config
from history import HistoryCommand
#contains defintion of the command classes to specific operations 

history = HistoryCommand()

class Command(ABC):
    @abstractmethod 
    def execute(self):
        pass 

class AddCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        answer = self.num1 + self.num2
        history.log_history(self.num1, self.num2, 'add', answer)
        return answer
    
    

#shows the command defintion for an addition command 
    
class SubtractCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        answer = self.num1 - self.num2
        history.log_history(self.num1, self.num2, 'subtract', answer)
        return answer
    
class MultiplyCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        if not isinstance(self.num1, (int,float)):
            raise TypeError()
        if not isinstance(self.num2, (int, float)):
            raise TypeError()
        answer = self.num1 * self.num2
        history.log_history(self.num1, self.num2, 'multiply', answer)
        return answer
    
class DivideCommand():
    def __init__(self, num1, num2):
        self.num1 = num1 
        self.num2 = num2

    def execute(self):
        if self.num2 == 0 :
            raise ZeroDivisionError()
        answer = self.num1 / self.num2
        history.log_history(self.num1, self.num2, 'divide', answer)
        return answer
    
    
class MenuCommand():
    def execute(self):
        menu = "The avaliable plugin commands are as follows: add, subtract, multiply, divide, greet, exit, and menu. To utilize these commands, simply format your input as either <number 1> <number 2> <command> or just the <command>, depending on what you want the program to do."
        print(menu)
        return menu  

class GreetCommand():
    def execute(self):
        greeting = "Greetings! Hello, Professor! Welcome to my calculator program."
        print(greeting)
        return greeting 