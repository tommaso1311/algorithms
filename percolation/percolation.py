from utils import *

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

	def find(self, p, q):

		return self.sites[p] == self.sites[q]

	def union(self, p, q):

		self.sites[p] = self.sites[q]



def main():

	p = percolation(10)
	print(p.sites)

	print(p.find(3, 8))
	p.union(3, 8)
	print(p.find(3, 8))

if __name__ == "__main__":
	main()