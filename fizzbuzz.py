#Fizzbuzz question for Koding internship application

number = 0

while number != 100:

	number += 1

	multThree = number % 3 == 0
	multFive = number % 5 == 0

	if multThree and multFive:
		print "Fizzbuzz"
	elif multThree:
		print "Fizz"
	elif multFive:
		print "Buzz"
	else:
		print number
