class BasketballPlayer():
    def __init__(self, name, nogames, scores):
        self.name = name
        self.nogames = nogames
        self.scores = scores
    def average_score(self):
        return self.scores / self.nogames
    def display_data(self):
        print(f"{self.name} has played {self.nogames} games with a total score of {self.scores} and has an average goals per game of {self.average_score()}")

player1 = BasketballPlayer("Yao Ming", 100, 2000)
player2 = BasketballPlayer("Michael Jordon", 31, 600)

player1.display_data()
print()
player2.display_data()
