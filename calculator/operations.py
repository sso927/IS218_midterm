from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand

class calculator_operations:
    def __init__(self):
        self.history = []

    def execute_command(self, command: str):
        from calculator import Calculator 
        result = command.execute()
        self.history.append(result)
        return result 