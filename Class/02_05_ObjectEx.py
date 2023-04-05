class School:

    # create instance variables
    def __init__(self, name, pupils, classroom):
        self.name = name
        self.pupils = pupils
        self.classroom = classroom

    # function to display information of a school
    def show_info(self):
        self.avg_classroom_size = round((self.pupils / self.classroom), 0)
        print(f"{self.name} has an average of {self.avg_classroom_size} pupils per classroom.")

if __name__ == "__main__":


    # allow user to define variables for first school
    print("Information for School #1")
    name = input("Enter the name of the school: ")
    pupils = int(input("How many pupils does the school have? "))
    classroom = int(input("How many classrooms does the school have? "))

    school1 = School(name, pupils, classroom)

    # calls the display method on the first object
    school1.show_info()

    print()

    # allow user to define variables for second school
    print("Information for School #2")
    name = input("Enter the name of the school: ")
    pupils = int(input("How many pupils does the school have? "))
    classroom = int(input("How many classrooms does the school have? "))

    school2 = School(name, pupils, classroom)

    # calls the display method on the second object
    school2.show_info()