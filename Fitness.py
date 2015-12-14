class Fitness:
	def __init__(self, m, v):
		self.mean = m
		self.stdev = v

	def __gt__(self, other):
		return (self.mean - self.stdev) > (other.mean - other.stdev)

	def __str__(self):
		return str(self.mean) + " +/- " + str(self.stdev)