class Car():
    def __init__(self, kpl, tank_vol):
        self.standard_kpl = kpl
        self.tank_vol = tank_vol

    def get_sd_range(self):
        """
        
        >>> c = Car(100, 20)
        >>> c.get_sd_range()
        2000
        """
        return self.standard_kpl * self.tank_vol

#Main Routine

if __name__ == "__main__":
    import doctest
    doctest.testmod(verbose = True)
    car1 = Car(20, 100)
    car2 = Car(24, 80)

    print("The typical range of car1 is", car1.get_sd_range(), "km")
    print("The typical range of car2 is", car2.get_sd_range(), "km")
    