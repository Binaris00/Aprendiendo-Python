"""
Encapsulation:
a. Create private attributes and methods in a class to restrict access and hide implementation details.
b. Use getters and setters to control access to attributes and ensure data consistency.
c. Create properties to allow accessing attributes like they were public but still control access.    
"""

class Navigator:
    """Class model for all navigators 
    """
    def __init__(self, name, theme, icon):
        """Atributes for class model

        Args:
            name (string): The name or names for the navigator
            theme (string): Colors for the navigator
            __admin_key (int): Key to enter the admin account
            icon (string): Description about the navigator icon
            _staff_members (string): All members for the navigator team
        """
        
        self.name = name
        self.theme = theme
        self.__admin_key = 12345
        self.icon = icon
        self._staff_members = "Red circle", "GoodAdmin, InfernalMod, Creeper69"
        
    def display_staff(self):
        """Display the protected attribute staff members
        """
        print(self._staff_members)
        
opera = Navigator("Opera", "Red, White", "Red circle")

"""
print(vars(opera))
print(opera.__admin_key)
"""

opera.display_staff()