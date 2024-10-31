from app.commands import DivideCommand

def execute(num1, num2):
    command = DivideCommand(num1, num2)
    return command.execute()