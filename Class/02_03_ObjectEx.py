class OneString:

    # define instance variable
    def __init__(self, my_string):
        self.my_string = my_string

    # print statement about objects storing strings
    def show_string(self):
        """
        >>> o = OneString("word")
        >>> o.show_string()
        This object stores word
        """

        print(f"This object stores {self.my_string}")

    # allows user to set the string of an object
    def set_string(self):
        self.my_string = input("Enter a word or sentence. ")

if __name__ == "__main__":

    # import doctest to check that the program works correctly
    import doctest
    doctest.testmod()

    # instantiate two OneString objects
    s1 = OneString("")
    s2 = OneString("")

    # allow user to set strings of objects
    s1.set_string()
    s2.set_string()

    print()

    # print statement about objects storing strings
    s1.show_string()
    s2.show_string()

    # define function to compare two strings
    def is_same(x, y):
        if x.my_string == y.my_string:
            return True
        
        else:
            return False