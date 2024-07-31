class Shoe:
    # now our method has 4 parameters (including self)!
    def __init__(self, brand, shoe_type, price):
        # we assign them accordingly
        self.brand = brand
        self.type = shoe_type
        self.price = price
        # the status is set to True by default
        self.in_stock = True

    def on_sale_by_percent(self, percent):
        self.price = self.price * (1 - percent)

# Create two shoe instances
skater_shoe = Shoe("Vans", "Low-top Trainers", 59.99)
dress_shoe = Shoe("Jack & Jill Bootery", "Ballet Flats", 29.99)
print(dress_shoe.price)
dress_shoe.on_sale_by_percent(0.6)
print(dress_shoe.price)

