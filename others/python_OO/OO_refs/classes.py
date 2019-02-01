# Learn Classes

# Ref:
# https://medium.com/the-renaissance-developer/python-101-object-oriented-programming-part-1-7d5d06833f26

# https://medium.com/the-renaissance-developer/python-101-object-oriented-programming-part-2-8e0db3ddd531


class Vehicle:
	
	def __init__(self, wheels, type_of_tank, seat_cap, max_vel):
		self.wheels = wheels
		self.type_of_tank = type_of_tank
		self.seat_cap = seat_cap
		self.max_vel = max_vel


	def wheel(self):
		return self.wheels
	
	def set_wheels(self, number):
		self.wheels = number
	
	def go(self):
		print("{} goes VRUUUUUUUM!".format(self.wheels))


tesla = Vehicle(4, 'electric', 5, 250)

print(tesla.wheels)
tesla.set_wheels(2) # its a motorbike now!
print(tesla.wheels)
print(tesla.go())

print("Done!")



