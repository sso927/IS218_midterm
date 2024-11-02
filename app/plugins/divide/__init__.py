from app.commands import DivideCommand
import logging 

def execute(num1, num2):
    command = DivideCommand(num1, num2)
    logging.info('Divide command working.')
    return command.execute()