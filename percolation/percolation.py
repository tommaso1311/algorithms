import numpy as np

class percolation:


	def __init__(self, N):

		self.sites = np.array([i for i in range(N*N+2)])
		self.sizes = np.ones(N*N+2)


	def open(self, row, column):

		pass


	def is_open(self, row, column):

		pass


	def is_full(self, row, column):

		pass


	def percolates(self):

		pass


	def root(self, i):

		while i != self.sites[i]:
			self.sites[i] = self.sites[self.sites[i]]
			i = self.sites[i]

		return i


	def connected(self, p, q):

		return self.root(p) == self.root(q)


	def union(self, p, q):

		i = self.root(p)
		j = self.root(q)

		if i == j:
			pass

		if self.sizes[i] < self.sizes[j]:
			self.sites[i] = j
			self.sizes[j] += self.sizes[i]
		else:
			self.sites[j] = i
			self.sizes[i] += self.sizes[j]


def main():

	p = percolation(4)
	print(p.sites)
	print(p.sizes)


if __name__ == "__main__":
	main()