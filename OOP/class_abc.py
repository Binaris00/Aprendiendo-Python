"""
Abstract Base Classes:
a. Use the abc module to define an abstract base class.
b. Implement abstract methods in derived classes.
c. Use isinstance() and issubclass() to check object and class inheritance.
"""

import abc

class Telephone(abc.ABC):
    """Base class for X cellphone

    Args:
        abc (Module): Module for create abstract class
    """
    @abc.abstractmethod
    def more_charge():
        pass
    
    @abc.abstractmethod
    def download_app():
        pass
    
    @abc.abstractmethod
    def call_number():
        pass
    
    @abc.abstractmethod
    def turn_off():
        pass
    
    @abc.abstractmethod
    def turn_on():
        pass

class Movistar(Telephone):
    """Base class for all movistar cellphones

    Args:
        abc (Module): Module for create abstract class
    """
    def more_charge(self):
        return f"Telephone charged!!"
    
    def download_app(self):
        return f"This app is now 90% downloaded"
    
    def call_number(self):
        return f"You want to call this number?"
    
    def turn_off(self):
        return f"The telephone is turned off"
    
    def turn_on(self):
        return f"The telephone is turned on"


class Samsung(Telephone):
    """Base class for all samsung cellphones

    Args:
        abc (Module): Module for create abstract class
    """
    def more_charge(self):
        return f"Telephone charged!!"
    
    def download_app(self):
        return f"This app is now 90% downloaded"
    
    def call_number(self):
        return f"You want to call this number?"
    
    def turn_off(self):
        return f"The telephone is turned off"
    
    def turn_on(self):
        return f"The telephone is turned on"

objects = Movistar()
print(isinstance(objects, Movistar))
print(issubclass(Movistar, Telephone))