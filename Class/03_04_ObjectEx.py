class House:

    # define instance variables
    def __init__(self, house_id, address, num_bedrooms, asking_price, area):
        self.house_id = house_id
        self.address = address
        self.num_bedrooms = num_bedrooms
        self.asking_price = asking_price
        self.area = area
        #self.display_price_per_area = -1
        #self.display_price_per_rooms = -1

    # method to show info of a house
    def show_info(self):
        '''
        This method displays the information of a house.
        For example:
        
        >>> h = House("DGB2353", "14 Orion Terrace", 2, 595000, 340)
        >>> h.show_info()
        ID: DGB2353   Address: 14 Orion Terrace
        Number of bedrooms: 2   Asking price: $595000
        Price by area: $1750
        Price per room: $297500
        ******
        '''

        print(f"ID: {self.house_id}   Address: {self.address}")
        print(f"Number of bedrooms: {self.num_bedrooms}   Asking price: ${self.asking_price}")

        # round price per area and price per room and convert to integer
        self.display_price_per_area = round(self.calculate_price_per_area())
        self.display_price_per_rooms = round(self.calculate_price_per_rooms())

        # print the rounded values
        print(f"Price by area: ${self.display_price_per_area}")
        print(f"Price per room: ${self.display_price_per_rooms}")

        print("******")

    # method to calculate price per area
    def calculate_price_per_area(self):
        '''
        This method calculates the price of a house per unit of area
        and returns the value. For example:

        >>> h = House("DGB2353", "14 Orion Terrace", 2, 595000, 340)
        >>> h.calculate_price_per_area()
        1750.0
        '''
        
        price_per_area = self.asking_price / self.area
        return price_per_area

    # method to calculate price per room
    def calculate_price_per_rooms(self):
        '''
        This method calculates the price of a house per bedroom and returns
        the value. For example:

        >>> h = House("DGB2353", "14 Orion Terrace", 2, 595000, 340)
        >>> h.calculate_price_per_rooms()
        297500.0
        '''
        
        price_per_rooms = self.asking_price / self.num_bedrooms
        return price_per_rooms

if __name__ == '__main__':

    # import doctest to check that code works correctly
    import doctest
    doctest.testmod()

    # create list to store House objects
    houses = []

    # hardcoded houses to append to house list
    houses.append(House("DGB2354", "22 Helens Rd", 4, 320000, 240))
    houses.append(House("DGB2355", "2 Aston Crescent", 3, 110000, 190))
    houses.append(House("DGB2356", "5 Stratton St", 5, 550000, 380))

    # loop through houses list to display info for each house
    for i in range (0, len(houses)):
        houses[i].show_info()