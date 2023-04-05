
class Person():
    def __init__(self, name, yob, gender):
        self.name = name
        self.yob = yob
        self.gender = gender
    def get_age(self):
        now = 2023
        
        return now - self.yob 
    def get_gender(self):
        if self.gender == True:
            return "Male"
        else:
            return "Female"
    def display_data(self):
        print(f"{self.name} is {self.get_gender()}, aged {self.get_age()} and was born in the year {self.yob}")



if __name__ == "__main__":
    person1 = Person("Joe", 2000, True)
    person2 = Person("Freda", 1990, False)
    person1.display_data()
    person2.display_data()
    
