class Car:
	def __init__(self, mark, model, year):
		self.mark = mark
		self.model = model
		self.year = year
		self.odometer = 0
		self.fuel = 70

	def drive(self, km):
		self.km = km
		self.add_distance(km)
		self.subtract_fuel(km)
		if self.fuel > 0:
			
			return f"{self.mark}--{self.model}--{self.year}. Let's drive!  You can drive {self.fuel * 10} km"
		else:
			return f"Need more fuel, please fill more!"

	def add_distance(self, km):
		self.odometer += km

	def subtract_fuel(self, km):
		self.fuel -= km / 10

car = Car(
	'Ford', 'f 250 raptor', '2019')

print(car.drive(690))