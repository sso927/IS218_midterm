from app.commands import AddCommand
import logging 

def execute(num1, num2):
    command = AddCommand(num1, num2)
    logging.info('Add command working.')
    return command.execute()

