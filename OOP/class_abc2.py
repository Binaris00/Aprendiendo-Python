"""
Abstract Base Classes:
a. Use the abc module to define an abstract base class.
b. Implement abstract methods in derived classes.
c. Use isinstance() and issubclass() to check object and class inheritance.
"""

"""This is the 2 file because I want to practice more :)"""
import abc

class app(abc.ABC):
    
    @abc.abstractmethod
    def close_app():
        pass
    
    @abc.abstractmethod
    def info():
        pass
    

class social_app(app):
    
    def close_app(self):
        return f"The app is closed"
    
    def info(self):
        return f"Name: Facebook, Created: 19-September-2000"


facebook = social_app()
print(isinstance(facebook, social_app))
print(issubclass(social_app, app))