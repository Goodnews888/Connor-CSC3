class Movie():
    def __init__(self, title, cost, revenue):
        self.title = title
        self.cost = cost
        self.revenue = revenue
    def display_data(self):
        print(f"Movie Title: {self.title}\nCost: {self.cost}\nRevenue: {self.revenue}")
    def net_profit(self):
        return self.revenue - self.cost

def main():
    movie1 = Movie("Avatar 1", 237000000, 2900000000)
    movie2 = Movie("Avatar 2", 250000000, 1585000000)
    movie1.display_data()
    print(f"Net profit is: {movie1.net_profit()}\n")
    movie2.display_data()
    print(f"Net profit is: {movie2.net_profit()}\n")
    

if __name__ == "__main__":
    main()