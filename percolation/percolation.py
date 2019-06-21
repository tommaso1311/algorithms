import numpy as np

class percolation:


	def __init__(self, N):

		self.N = N
		self.sites = [None]*(N*N+2)
		self.sites[0] = 0
		self.sites[-1] = N*N+1
		self.sizes = [0]*(N*N+2)
		self.sizes[0] = 1
		self.sizes[-1] = 1


	def open(self, index):

		self.sites[index] = index
		self.sizes[index] = 1

		top = index-self.N if index-self.N >=0 else 0
		bottom = index+self.N if index+self.N <= self.N*self.N else self.N*self.N+1
		left = index-1 if (index-1)%self.N != 0 else None
		right = index+1 if index%self.N != 0 else None

		adj = [top, right, bottom, left]
		adj = [x for x in adj if x != None]

		for site in adj:
			if self.sites[site] != None: self.union(index, site)


	def is_open(self, index):

		if self.sites[index] is None: return False
		else: return True


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

	N = 1000
	p = percolation(N)
	
	while not p.percolates():

		index = np.random.randint(1, N*N+1)

		if not p.is_open(index): p.open(index)

	print(1-len([x for x in p.sites if x is None])/(N*N))

if __name__ == "__main__":
	main()