# Check to see if a string is a palindrome
# Uses extended slice syntax => [begin:end:step]; leave off begin and end to
# reverse a string
def is_palindrome(s):
	return (s == s[::-1])

if __name__ == "__main__":
	s = raw_input("Enter a string: ")
	print(is_palindrome(s))