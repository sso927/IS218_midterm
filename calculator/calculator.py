from calculator.operations import calculator_operations
from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand


class Calculator:
    def __init__(self):
        self.operations = Calculator.operations()

    def add(self, a,b):
        return self.operations.execute_commands(AddCommand, a, b)
    
    def subtract(self, a,b):
        return self.operations.execute_commands(SubtractCommand, a, b)
    
    def multiply(self, a,b):
        return self.operations.execute_commands(MultiplyCommand, a, b)
    
    def divide(self, a,b):
        return self.operations.execute_commands(DivideCommand, a, b)