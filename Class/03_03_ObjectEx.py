class Actor:

    # create gender instance variable (defaults to male)
    def __init__(self):
        self.gender = "male"

    # method to change gender to female
    def set_female(self):
        self.gender = "female"

    # method to print gender of actor
    def show_gender(self):
        print(self.gender)

if __name__ == '__main__':

    # create a list to store actor objects
    actor_list = []

    # constant to determine number of actors
    LIST_SIZE = 35

    # create actors in a loop
    for i in range(0, LIST_SIZE):
        new_actor = Actor()
        actor_list.append(new_actor)

    # call the set_female method on every 5th actor
        # divisibility test on i+1
        if (i + 1) % 5 == 0:
            actor_list[i].set_female()

    # print gender of actors in a loop
    for i in range(0, LIST_SIZE):
        actor_list[i].show_gender()