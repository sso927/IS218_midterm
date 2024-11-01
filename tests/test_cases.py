#using direct function calls 

import pytest
from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand
from app.commands import GreetCommand
from app.commands import MenuCommand

def test_case_greet_command():
    command = GreetCommand()
    result = command.execute()
    assert result == "Greetings! Hello, Professor! Welcome to my calculator program."


def test_case_menu_command():
    command = MenuCommand()
    result = command.execute()
    assert result == "The avaliable plugin commands are as follows: add, subtract, multiply, divide, greet, exit, and menu. To utilize these commands, simply format your input as either <number 1> <number 2> <command> or just the <command>, depending on what you want the program to do.\nView your calculation history by inputting 'history' or 'clear'."
    
def test_case1_add_command():
    command = AddCommand(10, 2)
    result = command.execute()
    assert result == 12, "The app did not provide the correct answer."


def test_case2_add_command():
     command = AddCommand(10, 'b')
     with pytest.raises(TypeError):
         command.execute()


def test_case3_add_command():
     command = AddCommand('b', 10)
     with pytest.raises(TypeError):
         command.execute()

def test_case1_subtract_command():
    command = SubtractCommand(10, 2)
    result = command.execute()
    assert result == 8, "The app did not provide the correct answer."


def test_case2_subtract_command():
     command = SubtractCommand(10, 'b')
     with pytest.raises(TypeError):
         command.execute()


def test_case3_subtract_command():
     command = SubtractCommand('b', 10)
     with pytest.raises(TypeError):
         command.execute()

def test_case1_multiply_command():
    command = MultiplyCommand(10, 2)
    result = command.execute()
    assert result == 20, "The app did not provide the correct answer."

def test_case2_multiply_command():
    command = MultiplyCommand(10, 'b')
    with pytest.raises(TypeError):
        command.execute()

def test_case3_multiply_command():
    command = MultiplyCommand('b', 10)
    with pytest.raises(TypeError):
        command.execute()

def test_case1_divide_command():
    command = DivideCommand(10, 2)
    result = command.execute()
    assert result == 5, "The app did not provide the correct answer."
   
def test_case2_divide_command():
     command = DivideCommand(10, 'b')
     with pytest.raises(TypeError):
         command.execute()

def test_case3_divide_command():
     command = DivideCommand('b', 10)
     with pytest.raises(TypeError):
         command.execute()

def test_case_dividebyzero_command():
    with pytest.raises(ZeroDivisionError):
        command = DivideCommand(10,0)
        command.execute()
    