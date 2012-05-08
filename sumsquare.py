# Given three numbers, print the sum of the squares of the two largest numbers
def sumsquare(a, b, c):
	nums = [a, b, c]
	sortnums = sorted(nums)
	return sortnums[-1]**2 + sortnums[len(sortnums)/2]**2

if __name__ == "__main__":
	nums = []
	num_string = raw_input("Enter three numbers separated by spaces: ")
	for v in num_string:
		if v != ' ':
			nums.append(int(v))
	print(sumsquare(nums[0], nums[1], nums[2]))