# import time
import percolation
import numpy as np
# import matplotlib.pyplot as plt

def threshold(N, T):

	thresholds = []

	for _ in range(T):

		model = percolation.percolation(N)

		while not model.percolates():

			index = np.random.randint(1, N*N+1)
			model.open(index)

		t = 1-len([x for x in model.sites if x is None])/(N*N)
		thresholds.append(t)

	m = np.mean(thresholds)
	s = np.std(thresholds)

	return m, s

def print_confidence_intervals(N, T):

	m, s = threshold(N, T)

	print("mean =", m)
	print("standard deviation =", s)
	print("confidence intervals (95%) =", m-1.96*s/np.sqrt(T), m+1.96*s/np.sqrt(T))

# N = [x for x in range(1, 201)]
# print(N)
# times = []

# for n in N:

# 	print(n)

# 	p = percolation.percolation(n)

# 	start = time.time()

# 	while not p.percolates():

# 		index = np.random.randint(1, n*n+1)

# 		if not p.is_open(index): p.open(index)

# 	finish = time.time()
# 	times.append(finish-start)

# plt.yscale("log")
# plt.xscale("log")
# plt.plot(N, times)
# plt.show()