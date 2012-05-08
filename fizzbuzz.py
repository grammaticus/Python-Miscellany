# Print numbers from 1 to input, substituting "Fizz" for numbers divisible by 3,
# "Buzz" for numbers divisible by 5, and "FizzBuzz" for numbers divisible by both
def fizzbuzz(n):
	for i in range(1, n+1):
		if (i%3 == 0) and (i%5 == 0):
			print "FizzBuzz"
		elif (i%3 == 0):
			print "Fizz"
		elif (i%5 == 0):
			print "Buzz"
		else:
			print "%d" %i

if __name__ == "__main__":
	num = int(raw_input("Enter a number: "))
	fizzbuzz(num)