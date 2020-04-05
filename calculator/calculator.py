class Calculator():
	def __init__(self, a, b):
		self.a = int(a)
		self.b = int(b)

	def add(self):
		return self.a + self.b

	def subtract(self):
		return self.a - self.b

	def multiple(self):
		return self.a * self.b

	def divide(self):
		return self.a / self.b