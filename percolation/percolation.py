import numpy as np

class percolation:
	"""
	Class used to compute percolation threshold

	Attributes
	----------
	N : int
		NxN is the number of sites in the model
	sites : list
		the sites of the model
	_sizes : list
		sizes of the connected sites

	Methods
	-------
	open(index)
		used to open a new site and connect it with adjacentes sites
	_is_open(index)
		returns if a site is open or not
	percolates()
		returns if the model percolates or not
	_root(i)
		returns the root of the i-th site
	_union(i, j)
		connects two sites
	"""


	def __init__(self, N):
		"""
		Parameters
		----------
		N : int
		"""

		self._N = N

		# initializing sites
		self.sites = [None]*(N*N+2)
		self.sites[0] = 0
		self.sites[-1] = N*N+1

		# initializing sizes
		self._sizes = [0]*(N*N+2)
		self._sizes[0] = 1
		self._sizes[-1] = 1


	def open(self, index):
		"""
		Parameters
		----------
		index : int
		"""

		if not self._is_open(index):

			self.sites[index] = index
			self._sizes[index] = 1

			# getting adjacent sites indices
			top = index-self._N if index-self._N >=0 else 0
			bottom = index+self._N if index+self._N <= self._N*self._N else self._N*self._N+1
			left = index-1 if (index-1)%self._N != 0 else None
			right = index+1 if index%self._N != 0 else None

			adj = [top, right, bottom, left]
			adj = [x for x in adj if x != None]

			for site in adj:
				if self.sites[site] != None: self._union(index, site)

		else:
			pass


	def _is_open(self, index):
		"""
		Parameters
		----------
		index : int
		"""

		if self.sites[index] is None: return False
		else: return True


	def percolates(self):

		return self._root(self.sites[0]) == self._root(self.sites[-1])


	def _root(self, i):
		"""
		Parameters
		----------
		index : int
		"""

		while i != self.sites[i]:
			self.sites[i] = self.sites[self.sites[i]]
			i = self.sites[i]

		return i


	def _union(self, p, q):
		"""
		Parameters
		----------
		p : int
		q : int
		"""

		i = self._root(p)
		j = self._root(q)

		if i == j:
			pass

		# connecting the smallest to the biggest
		if self._sizes[i] < self._sizes[j]:
			self.sites[i] = j
			self._sizes[j] += self._sizes[i]
		else:
			self.sites[j] = i
			self._sizes[i] += self._sizes[j]


if __name__ == "__main__":
	print("This is a library not a program!")