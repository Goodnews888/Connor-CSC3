#Design and write a class representing a country. It should have:
#an __init__ method for the class. a method which displays the data.
#Design and write a main routine which creates some country
#objects and displays their data.
#Let your display method fulfill the following doctest (or something similar):
class Country():
    def __init__(self, name, continent, leader, population, capital, land_area):
        self.name = name
        self.continent = continent
        self.leader = leader
        self.population = population
        self.capital = capital
        self.land_area = land_area
    def display_data(self):
        """
        >>> country1 = Country("New Zealand", "Oceania", "Chris Hipkins", 5123000, "Wellington", 268021)
        >>> country1.display_data()
        Name: New Zealand
        Continent: Oceania
        Leader: Chris Hipkins
        Population: 5123000
        Capital: Wellington
        Land Area: 268021 km^2
        >>> country2 = Country("Australia", "Oceania", "Anthony Albanese", 25690000, "Canberra", 7688000)
        >>> country2.display_data()
        Name: Australia
        Continent: Oceania
        Leader: Anthony Albanese
        Population: 25690000
        Capital: Canberra
        Land Area: 7688000 km^2
        """
        print(f"Name: {self.name}\nContinent: {self.continent}\nLeader: {self.leader}\nPopulation: {self.population}\nCapital: {self.capital}\nLand Area: {self.land_area} km^2")
    def population_density(self):
        return self.population / self.land_area


def main():
    country1 = Country("New Zealand", "Oceania", "Chris Hipkins", 5123000, "Wellington", 268021)
    country2 = Country("Australia", "Ocenia", "Anthony Albanese", 25690000, "Canberra", 7688000)

    country1.display_data()
    print(f"The population density of this country is: {country1.population_density()}")
    print()
    country2.display_data()
    print(f"The population density of this country is: {country2.population_density()}")

if __name__ == "__main__":
    import doctest
    doctest.testmod()
    main()


    
   
