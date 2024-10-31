from app.commands import MultiplyCommand

def execute(num1, num2):
    command = MultiplyCommand(num1, num2)
    return command.execute()