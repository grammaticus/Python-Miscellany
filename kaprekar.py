# Kaprekar Number - consider an n-digit number k; square it and add the right n
# digits to the left n or n-1 digits; if it equals k, then k is a Kaprekar Number
def is_kaprekar(k):
	if k < 10:
		if k == 1 or k == 9:
			return True
		else:
			return False
	else:
		n = len(str(k))
		k_sqr = str(k**2)
		k_sqr_left = k_sqr[n-n%2:]
		k_sqr_right = k_sqr[:n-n%2]
		k_summed = int(k_sqr_left) + int(k_sqr_right)
		return k == k_summed
	return False

if __name__ == "__main__":
	k = int(raw_input("Enter a number: "))
	print(is_kaprekar(k))