digits_as_strings = {1: "One", 2: "Two", 3: "Three", 4: "Four", 5: "Five", 6: "Six", 
						7: "Seven", 8: "Eight", 9: "Nine"}

tens_as_strings = {2: "Twenty", 3: "Thirty", 4: "Forty", 5: "Fifty", 6: "Sixty",
						7: "Seventy", 8: "Eighty", 9: "Ninety"}

teens_as_strings = {10: "Ten", 11: "Eleven", 12: "Twelve", 13: "Thirteen",
						14: "Fourteen", 15: "Fifteen", 16: "Sixteen",
						17: "Seventeen", 18: "Eighteen", 19: "Nineteen"}

def ninetynine_bottles():
	n = 99
	while n > 0:
		tens = n/10
		if tens > 0:
			ones = n%(tens*10)
		else:
			ones = n
		if tens > 1 and ones != 0:
			bottles = tens_as_strings[tens] + '-' + digits_as_strings[ones].lower()
		elif tens > 1 and ones == 0:
			bottles = tens_as_strings[tens]
		elif tens == 1:
			bottles = teens_as_strings[n]
		else:
			bottles = digits_as_strings[ones]
		if n != 99 and n != 1:
			print "%s bottles of beer on the wall!" %bottles
		if n > 1:
			print "\n%s bottles of beer on the wall, %s bottles of beer!" %(bottles, bottles.lower())
			print "Take one down, pass it around!"
		elif n == 1:
			print "\n%s bottle of beer on the wall, %s bottle of beer!" %(bottles, bottles.lower())
			print "Take it down, pass it around!"
			print "No more bottles of beer on the wall!"
		n-=1

if __name__ == "__main__":
	ninetynine_bottles()