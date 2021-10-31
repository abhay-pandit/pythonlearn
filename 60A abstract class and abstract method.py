'''
abstract = निराकार,bodiless

abstract class and method not supported  in python but we can use a module for it
'''

from abc import ABC, abstractmethod

class Computer(ABC):            #Abstract Class
    @abstractmethod
    def process(self):          #abstract Method
        pass




c1 = Computer()
c1.flow()