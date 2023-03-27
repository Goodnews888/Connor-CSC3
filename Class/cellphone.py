class Cellphone():
    def __init__(self, model,  price):
        self.model = model
        self.price = price
    def display_data(self):
        print(f"Model: {self.model}\nPrice: {self.price}")
    def depreciated_value(self):
        depreciated_price = self.price
        for _ in range(2):
            depreciated_price *= 0.67
        return depreciated_price

def main():
    cellphone1 = Cellphone("iPhone 6", 1399)
    cellphone2 = Cellphone("iPhone 8", 500)
    cellphone1.display_data()
    print(f"Depreciated value after 2 years: {cellphone1.depreciated_value()}\n")
    cellphone2.display_data()
    print(f"Depreciated value after 2 years: {cellphone2.depreciated_value()}\n")

if __name__ == "__main__":
    main()