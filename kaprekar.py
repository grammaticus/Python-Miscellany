# Kaprekar Number - consider an n-digit number k; square it and add the right n
# digits to the left n or n-1 digits; if it equals k, then k is a Kaprekar Number
def is_kaprekar(k):
	if k == 1:
		return True
	elif k > 8:
		n = len(str(k))
		k_sqr = k**2
		k_sqr_str = str(k_sqr)
		k_sqr_left = k_sqr_str[n:]
		k_sqr_right = k_sqr_str[:n]
		k_summed = int(k_sqr_left) + int(k_sqr_right)
		return k == k_summed
	return False

if __name__ == "__main__":
	k = int(raw_input("Enter a number: "))
	print(is_kaprekar(k))