
class Car:
	def __init__(self, wheel, seat_cap, max_vel):
		self.wheel = wheel
		self.seat_cap = seat_cap
		self.max_vel = max_vel



#my_car = Car(4, 5, 250)
#print(my_car.wheel)
#print(my_car.seat_cap)
#print(my_car.max_vel)

# Inheritence
class ElectricCar(Car):
	def __init__(self, wheel, seat_cap, max_vel):
		# super class
		Car.__init__(self, wheel, seat_cap, max_vel)

my_elec_car = ElectricCar(10, 6, 300)

print(my_elec_car.wheel)
print(my_elec_car.seat_cap)
print(my_elec_car.max_vel)


