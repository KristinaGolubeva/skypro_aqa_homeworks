class Mailing:

    def __init__(self, address_to, address_from, cost, track):
        self.address_to = address_to
        self.address_from = address_from
        self.cost = cost
        self.track = track 

    def Path(self):
        to_ = self.address_to.mail()
        from_ = self.address_from.mail()
        print("Отправление", self.track, "из", from_, "в", to_, ". Стоимость", self.cost, "рублей.")


