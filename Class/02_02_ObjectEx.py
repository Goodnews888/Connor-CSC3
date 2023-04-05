class OneString:

    # define instance variable
    def __init__(self, my_string):
        self.my_string = my_string

    def show_string(self):
        """
        >>> o = OneString("word")
        >>> o.show_string()
        This object stores word
        """

        print(f"This object stores {self.my_string}")

if __name__ == "__main__":

    # import doctest to check that the program works correctly
    import doctest
    doctest.testmod()

    # instantiate two strings
    s1 = OneString("hello")
    s2 = OneString("world")

    # print statement about objects storing strings
    s1.show_string()
    s2.show_string()

    # define function to compare two strings
    def is_same(x, y):
        if x.my_string == y.my_string:
            return True
        
        else:
            return False