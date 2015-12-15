class Fitness:
	def __init__(self, m, v):
		self.mean = m
		self.stdev = v

	def __gt__(self, other):
		return float(self) > float(other)

	def __float__(self):
		return self.mean - self.stdev

	def __str__(self):
		return str(float(self)) + " " + str(self.mean) + " +/- " + str(self.stdev)