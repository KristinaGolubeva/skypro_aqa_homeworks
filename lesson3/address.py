class Address:
    index = "000000"
    city = 'City'
    street = 'Street'
    house = "00"
    apartment = "00"

    def __init__(self, my_index, my_city, my_street, my_house, my_apartment):
        self.index = my_index
        self.city = my_city
        self.street = my_street
        self.house = my_house
        self.apartment = my_apartment
    
    def mail(self):
        return self.index + "," + self.city + "," + self.street + "," + self.house + "-" + self.apartment



