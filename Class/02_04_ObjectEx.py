class TeamSport:

    # create instance variables by calling the store_info method
    def __init__(self):
        self.store_info()

    # method to get info for the sport
    def store_info(self):
        self.sport_name = input("What is the name of a team sport? ")
        self.num_players = input(f"How many players are there in a {self.sport_name} team? ")

    # method to print info for a chosen sport
    def show_info(self):
        print(f"{self.sport_name} is a team sport.")
        print(f"There are {self.num_players} players in a {self.sport_name} team.")

if __name__ == "__main__":

    # instantiate two sports
    ts1 = TeamSport()
    ts2 = TeamSport()

    # print info of each team sport
    ts1.show_info()
    ts2.show_info()