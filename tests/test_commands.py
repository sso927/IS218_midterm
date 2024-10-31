#test commands separately --> can use similar code as hw for this part
#using direct function calls 

import pytest
from app import App

from app.commands import AddCommand
from app.commands import SubtractCommand
from app.commands import MultiplyCommand
from app.commands import DivideCommand

def testcase_greetcommand(capfd, monkeypatch):
    inputs = iter(['greet', 'exit'])
    monkeypatch.setattr('builtins.input', lambda _: next(inputs))

    app = App()
    with pytest.raises(SystemExit) as e:
        app.start()

    assert str(e.value) == 'Exiting...', 'The app did not exit as expected.'

def test_case_add_command():
    command = AddCommand(10, 2)
    result = command.execute
    assert result == 15, "The app did not provide the correct answer."

def test_case_subtract_command():
    command = SubtractCommand(10, 2)
    result = command.execute
    assert result == 8, "The app did not provide the correct answer."

def test_case_multiply_command():
    command = MultiplyCommand(10, 2)
    result = command.execute
    assert result == 20, "The app did not provide the correct answer."

def test_case_divide_command():
    command = DivideCommand(10, 2)
    result = command.execute
    assert result == 5, "The app did not provide the correct answer."
   

def test_case_dividebyzero_command():
    command = DivideCommand(10, 0)
    result = command.execute
    assert result == ZeroDivisionError, "The app did not provide the correct answer."
   
   

