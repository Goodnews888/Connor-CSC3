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

    # create list to store school objects
    school_list = []

    # constant to control how many schools are asked for (must be integer)
    NO_OF_SCHOOLS = 2

    # use loop to ask user for school information
    for i in range (1, NO_OF_SCHOOLS+1):
        print("Information for School #{}:".format(i))
        name = input("Enter the name of the school: ")
        roll = int(input("How many pupils does the school have? "))
        classroom = int(input("How many classrooms does the school have? "))

        school = School(name, roll, classroom)
        school_list.append(school)

        print()
        
    # use loop to display information for each school
    for i in range (0, NO_OF_SCHOOLS):
        school_list[i].show_info()

    

    