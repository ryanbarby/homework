class Fibbonacci:
	input = int(input("Please enter a number."))
	def fib(input):
		firstnum = 0
		secondnum = 1
		for num in range(0,input):
			print(firstnum)
			thirdnum = firstnum
			firstnum = secondnum
			secondnum = thirdnum + secondnum
		print(firstnum)
	fib(input)
Fibbonacci()		
