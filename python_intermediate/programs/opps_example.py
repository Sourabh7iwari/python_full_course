
class Vehicle:
    def __init__(self,cc,seats,milage, fuel_efficency) -> None:
        self.cc = cc
        self.seats=seats
        self.milage=milage
        self.fuel_efficency=fuel_efficency
    
# Price calculator method
    def price(self) -> float:#+
        price = (self.cc * 500) + (self.seats * 1000) - (self.milage * 0.01) + (5000 if self.fuel_efficency > 25 else 0)
        return price

cc = 1000
seats = 5
milage = 20000
fuel_efficency = 40

# When
vehicle = Vehicle(cc, seats, milage,fuel_efficency)

# Then
price=vehicle.price()
print(price)