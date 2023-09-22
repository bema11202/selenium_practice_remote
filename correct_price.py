class house():
    """This class is used to create a house object"""
    company_name = "Awesome building company"

    inflation_coefficient = 1.08

    def __init__(self, address, state, alarm, price):
        self.address = address
        self.state = state
        self.Alarm = alarm
        self.price = price

    def correctPriceMethod(self):
        self.price *= self.inflation_coefficient

#-----------------------------------------------------------

apartment1 = house(1234, "california", False , 350000)
apartment2 = house(1234, "california", False , 360000)
apartment3Price = 300000

apartment1.correctPriceMethod()
apartment2.correctPriceMethod()

#-----------------------------------------------------------
print(apartment1.price)
print(apartment2.price)
print(apartment2.company_name)
print(apartment1.price)
