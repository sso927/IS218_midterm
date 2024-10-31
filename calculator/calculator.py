from app.plugins.add import execute as addplugin
from app.plugins.subtract import execute as subtractplugin
from app.plugins.multiply import execute as multiplyplugin
from app.plugins.divide import execute as divideplugin

class Calculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return addplugin(a,b)

    def subtract(self, a, b):
        return subtractplugin(a,b)
    
    def multiply(self, a, b):
        return multiplyplugin(a,b)
    
    def divide(self, a, b):
        return divideplugin(a,b)
    

'''from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand

#contains methods that instantiate the command clases and executes them --> simplifes the execution, streamlining the functionality 

class Calculator:
    def __init__(self):
        pass

    #provides methods and creates an instance of the AddCommand class to execute it.. the command.execute() calls the method that executes the specific action that encapsualtes the operation
    def add(self, a,b):
        command = AddCommand(a,b)
        return command.execute()
    
    def subtract(self, a,b):
        command = SubtractCommand(a,b)
        return command.execute()
    
    def multiply(self, a,b):
        command = MultiplyCommand(a,b)
        return command.execute()
    
    def divide(self, a,b):
        command = DivideCommand(a,b)
        return command.execute()
    
'''