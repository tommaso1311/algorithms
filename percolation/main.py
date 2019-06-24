import numpy as np
import argparse
import stats

def main():

	parser = argparse.ArgumentParser()

	parser.add_argument("N", action="store", help="NxN is number of sites", type=int)
	parser.add_argument("T", action="store", help="number of tests", type=int)
	parser.add_argument("-v", "--verbose", action="store_true", help="prints the time")

	args = parser.parse_args()

	stats.print_threshold_confidence_intervals(args.N, args.T, args.verbose)

if __name__ == "__main__":
	main()