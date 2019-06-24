import time
import numpy as np
import percolation


def stats(N, T):

	thresholds = []
	times = []

	for _ in range(T):

		model = percolation.percolation(N)
		start = time.time()

		while not model.percolates():

			index = np.random.randint(1, N*N+1)
			model.open(index)

		finish = time.time()

		threshold = 1-len([x for x in model.sites if x is None])/(N*N)
		thresholds.append(threshold)
		times.append(finish-start)

	mean_thresholds = np.mean(thresholds)
	std_thresholds = np.std(thresholds)

	mean_time = np.mean(times)

	return mean_thresholds, std_thresholds, mean_time


def print_threshold_confidence_intervals(N, T, v):

	m, s, t = stats(N, T)

	print("mean threshold =", m)
	print("standard deviation =", s)
	print("confidence intervals (95%) =", m-1.96*s/np.sqrt(T), m+1.96*s/np.sqrt(T))

	if v:
		print("mean time taken =", t)


if __name__ == "__main__":
	print("This is a library not a program!")