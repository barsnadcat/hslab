class Fitness:
	def __init__(self, m, v):
		self.mean = m
		self.stdev = v

	def __gt__(self, other):
		return self.mean > other.mean

	def __str__(self):
		return str(self.mean) + " +/- " + str(self.stdev)