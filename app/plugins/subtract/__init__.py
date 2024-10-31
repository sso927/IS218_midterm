from app.commands import SubtractCommand

def execute(num1, num2):
    command = SubtractCommand(num1, num2)
    return command.execute()