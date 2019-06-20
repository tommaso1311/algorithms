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

		top = (row-1)*self.N + column + 1 if row > 0 else 0
		bottom = (row+1)*self.N + column + 1 if row < self.N-1 else self.N*self.N+1
		left = (row)*self.N + column if column > 0 else None
		right = (row)*self.N + column + 2 if column < self.N-1 else None

		adj = [left, top, right, bottom]

		for space in adj:
			if self.is_open(space): self.union(index, space)


	def is_open(self, index):

		if index == None:
			return False
		else:
			return self.opened[index]		


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
	p.open(1, 2)
	p.open(2, 2)
	p.open(2, 3)
	p.open(3, 3)
	p.open(0, 1)
	p.open(0, 2)
	print(p.percolates())


if __name__ == "__main__":
	main()