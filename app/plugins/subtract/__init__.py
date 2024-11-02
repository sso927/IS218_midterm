from app.commands import SubtractCommand
import logging

def execute(num1, num2):
    command = SubtractCommand(num1, num2)
    logging.info('Subtract command working.')
    return command.execute()