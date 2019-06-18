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

	def connected(self, p, q):

		return self.sites[p] == self.sites[q]

	def union(self, p, q):

		for i in range(len(self.sites)):

			pid = self.sites[p]
			qid = self.sites[q]

			if self.sites[i] == pid:
				self.sites[i] = qid



def main():

	p = percolation(10)
	print(p.sites)

	p.union(3, 8)
	p.union(8, 5)

	print(p.sites)

if __name__ == "__main__":
	main()