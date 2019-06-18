import numpy as np

class percolation:


	def __init__(self, N):

		self.sites = np.array([i for i in range(N+2)])


	def open(self, row, column):

		pass


	def is_open(self, row, column):

		pass


	def is_full(self, row, column):

		pass


	def percolates(self):

		pass

def main():

	p = percolation(10)
	print(p.sites)

if __name__ == "__main__":
	main()