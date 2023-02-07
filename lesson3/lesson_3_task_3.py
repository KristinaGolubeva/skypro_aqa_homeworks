from address import Address
from mailing import Mailing

address_to = Address("123456", " Almaty", " Shevchenko", " 15", "5")
address_from = Address("657432", " St.Petersburg", " Pulkovskoe", " 31/3", "128")
address_to.mail()
address_from.mail()

my_path = Mailing(address_to, address_from, 150, "Бандероль")
my_path.Path()

