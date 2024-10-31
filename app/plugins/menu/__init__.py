from app.commands import Command
import logging 

class MenuCommand(Command):
    def execute(self):
        print(f"The avaliable plugin commands are as follows: add, subtract, multiply, divide, greet, exit, and menu. 
              To utilize these commands, simply format your input as either <number 1> <number 2> <command> or just the <command>, depending
              on what you want the program to do.")
    logging.info('Menu command displayed with instructions.')