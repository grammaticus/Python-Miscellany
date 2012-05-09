# Given three numbers, print the sum of the squares of the two largest numbers
import sys

def sumsquare(a, b, c):
	nums = [a, b, c]
	sortnums = sorted(nums)
	return sortnums[-1]**2 + sortnums[len(sortnums)/2]**2

if __name__ == "__main__":
	nums = []
	num_string = raw_input("Enter three numbers separated by spaces: ")
	for v in num_string:
		if v != ' ':
			try:
				nums.append(int(v))
			except ValueError:
				print("You must enter three numbers")
				sys.exit(0)
	if len(nums) > 3:
		print("You must enter three numbers")
		sys.exit(0)
	try:
		print(sumsquare(nums[0], nums[1], nums[2]))
	except IndexError:
		print("You must enter three numbers")
		sys.exit(0)