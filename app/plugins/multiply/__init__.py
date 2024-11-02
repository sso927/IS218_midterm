from app.commands import MultiplyCommand
import logging 

def execute(num1, num2):
    command = MultiplyCommand(num1, num2)
    logging.info('Multiply command working.')
    return command.execute()