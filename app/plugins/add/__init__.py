from app.commands import AddCommand

def execute(num1, num2):
    command = AddCommand(num1, num2)
    return command.execute()

