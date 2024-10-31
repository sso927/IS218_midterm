from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand

#contains methods that instantiate the command clases and executes them --> simplifes the execution, streamlining the functionality 

class Calculator:
    def __init__(self):
        pass

    #provides methods and creats an instance of the AddCommand class to execute it.. the command.execute() calls the method that executes the specific action that encapsualtes the operation
    def add(self, a,b):
        command = AddCommand(a,b)
        return command.execute()
    
    def subtract(self, a,b):
        command = AddCommand(a,b)
        return command.execute()
    
    def multiply(self, a,b):
        command = AddCommand(a,b)
        return command.execute()
    
    def divide(self, a,b):
        command = AddCommand(a,b)
        return command.execute()
    
