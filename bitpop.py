#Count number of '1' bits in a string

def bit_population(s):
	pop = 0
	for v in s:
		if v == "1":
			pop+=1
	return pop

if __name__ == "__main__":
	bitstring = raw_input("Input a binary string: ")
	print(bit_population(bitstring))
