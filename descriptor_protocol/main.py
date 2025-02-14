class Person:
    """
    A class to represent a person.

    Attributes:
    name (str): The name of the person.
    age (int): The age of the person.
    experiance (int): The years of experience of the person.
    """

    def __init__(self, name: str, age: int, experiance: int) -> None:
        """
        Initializes a new Person instance.

        Parameters:
        name (str): The name of the person.
        age (int): The age of the person.
        experiance (int): The years of experience of the person.
        """
        self.name = name
        self.age = age
        self.experinace = experiance
        
    # the dender methods 
    def __repr__(self) -> str:
        """
        Returns an unambiguous string representation of the Person instance.

        This string can be used to recreate the object.
        """
        return f"name: {self.name}, age: {self.age}, experiance: {self.experinace}"
    
    def __str__(self) -> str:
        """
        Returns a readable string representation of the Person instance.

        This string provides a description of the person.
        """
        return f"His/Her name is {self.name}, he/she has an experiance of {self.experinace} years."
    




person1 = Person("Alice", 23, 3)
print(person1)              # prints a string about alice not a memory address of the object

print(person1.__repr__())