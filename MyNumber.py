# make a class called mynumber
class MyNumber:
    """
    This class stores a number and performs basic mathematics on the number.
    
    Attributes
    ----------
    x : int
        The number that this class works with.

    Methods
    -------
    print():
        Prints the number    
    add(y):
        Adds the number in y to the number of this object.
    subtract(y):
        Subtacts the number in y to the number of this object.
    """

    def __init__(self, x):

        """
    The function "__init__(self, x)" is the initial fucntion of the class MyNumber. 
    The input needs to be int, since some functions in this class required the input to be int. 
    if not, the command line will break and show the warning sign    

    Parameters
    ----------
    x : int
    the input need to be int

    Returns
    -------
    Exception message: "Please provide an integer when using the MyNumber object. If the x is not int, a warning will show up to warn user 

	   """

        if not type(x) == int:
            raise Exception("Please provide an integer when using the MyNumber object")
        self.x = x

    def print(self):

        """
    The function "print(self)" is used to print the variable passed from __init__function

    Parameters
    ----------

    Returns
    -------
    text: "The number is: "self.x"
        """
        print("The number is: {}".format(self.x))
        
    def add(self, y):
        """
    This function is used to make a "add" calculation to the self.x

    Parameters
    ----------
    y: int

    Returns
    -------
    int:  "self.x" will have the new number
        """

        self.x = self.x + y

    def subtract(self, y):
        """ 
    This function is used to make a "subtract" calculation to the self.x

    Parameters
    ----------
    y: int

    Returns
    -------
    int:  "self.x" will have the new number
        """
        self.x = self.x - y


def main():
    """ 
    This function is used to store the demonstration but without affecting the usage of this python file

    Parameters
    ----------
    xval = 3: int
    yval = 2: int

    Returns
    -------
    it will retun the following output:
    
    The number is: 2
    The number is: 4
    The number is: 2

    """

    xval = 3
    yval = 2
    number = MyNumber(2)
    number.print()
    number.add(yval)
    number.print()
    number.subtract(yval)
    number.print()

if __name__ == "__main__":
    main()
