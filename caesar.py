# Caesar cipher
import string
def encrypt(s, n):
	letters = string.ascii_uppercase
	s_encrypted = ""
	key = {}
	for i in range(0, 26):
		key.update({letters[i]:letters[(i+n)%26]})
	for v in s.upper():
		s_encrypted+=key[v]
	return s_encrypted

if __name__ == "__main__":
	s = raw_input("Enter a string to encrypt: ")
	n = int(raw_input("Enter an offset number: "))
	print "%s shifted %d is %s" %(s, n, encrypt(s, n))