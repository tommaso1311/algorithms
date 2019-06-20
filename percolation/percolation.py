import numpy as np

class percolation:


	def __init__(self, N):

		self.N = N
		self.sites = np.array([i for i in range(N*N+2)])
		self.sizes = np.ones(N*N+2)

		self.opened = [False]*(N*N+2)
		self.opened[0] = True
		self.opened[-1] = True


	def open(self, row, column):

		index = (row)*self.N + column + 1

		self.opened[index] = True


	def is_open(self, row, column):

		index = (row)*self.N + column + 1

		return self.opened[index]


	def is_full(self, row, column):

		pass


	def percolates(self):

		return self.root(self.sites[0]) == self.root(self.sites[-1])


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
	print(p.opened)
	p.open(1, 1)
	print(p.opened)
	print(p.is_open(1, 1))


if __name__ == "__main__":
	main()