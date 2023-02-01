class User:

    first_name = "nofname"
    second_name = "nosname"

    def __init__(self, fn, sn):
        self.first_name = fn
        self.second_name = sn

    def sayFirstName(self):
        print(self.first_name)
    
    def saySecondName(self):
        print(self.second_name)

    def sayBoth(self):
        print(self.first_name, self.second_name)
