import sys

def sort_even_odd(x):
	x.sort()
	for v in x:
		try:
			if v%2 == 1:
				tmp = v
				x.remove(v)
				x.append(tmp)
		except ValueError:
			print("You may only enter numbers")
			sys.exit(0)
	return x

if __name__ == "__main__":
	nums = raw_input("Enter a list of numbers separated by spaces: ")
	num_list = []
	for v in nums:
		if v != " ":
			num_list.append(int(v))
	print(sort_even_odd(num_list))