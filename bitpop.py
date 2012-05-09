#Count number of '1' bits in a string
import sys

def bit_population(s):
	pop = 0
	if s.count("1") + s.count("0") != len(s):
		print("You must enter a binary string")
		sys.exit(0)
	pop = s.count("1")
	return pop

if __name__ == "__main__":
	bitstring = raw_input("Input a binary string: ")
	print(bit_population(bitstring))
