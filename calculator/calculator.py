from app.plugins.add import execute as addplugin
from app.plugins.subtract import execute as subtractplugin
from app.plugins.multiply import execute as multiplyplugin
from app.plugins.divide import execute as divideplugin

class Calculator:
    def __init__(self):
        pass
    
    def add(self, a, b):
        return addplugin(a,b)

    def subtract(self, a, b):
        return subtractplugin(a,b)
    
    def multiply(self, a, b):
        return multiplyplugin(a,b)
    
    def divide(self, a, b):
        return divideplugin(a,b)
