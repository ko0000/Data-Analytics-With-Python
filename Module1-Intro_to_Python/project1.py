"""
This file performs a basic calculation (plus and minus) on the input number

Author: Itsuhiro Ko AFS505

Default Command-line usage:
    python project1.py #this will run a sample, check "main()"
    
    python project1.py 100
"""

class MyNumber:

    def __init__(self, x):
        if not type(x) == int:
            raise Exception("Please provide an integer when using the MyNumber object")
        self.x = x

    def print(self):
        print("The number is: {}".format(self.x))
        
    def add(self, y):
        self.x = self.x + y

    def subtract(self, y):
        self.x = self.x - y

def main():

    """
This function give an example of how to use the class "MyNumber"

Attributes
----------
xval = 3 : int
    The number that this class didn't work with.

yval = 2 : int
    The number that this class works with.

number : class
    The class that have a input int "2"

Methods
-------
print():
    Prints the number    
add(y):
    Adds the number in y to the number of this object.
subtract(y):
    Subtacts the number in y to the number of this object.
    """
    fileread=open("./data/covtype.data")
    xval = 3
    yval = 2
    number = MyNumber(2)
    number.print()
    number.add(yval)
    number.print()
    number.subtract(yval)
    number.print()
    print(type(number))
    
if __name__ == "__main__":
    main()