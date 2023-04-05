class Helicopter:

    # define instance variable
    def __init__(self, number):
        self.number = number

    # define up and down methods to print stuff in terminal
    def down(self):
        print(self.number, "down")

    def up(self):
        print(self.number, "up")

if __name__ == '__main__':

    # list to store helicopter objects
    helicopter_collection = []

    # create 100 helicopter objects in a loop
    for i in range(1, 101):
        new_helicopter = Helicopter(i)
        helicopter_collection.append(new_helicopter)

    # call the up method on the first 50 helicopters
    for i in range(0, 50):
        helicopter_collection[i].up()

    # call the down method on the next 50 helicopters
    for i in range(50, 100):
        helicopter_collection[i].down()