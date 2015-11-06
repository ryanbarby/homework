class triangles():
	def triangle(number):
		for item in range(1, number + 1):
			print("." * item)
	def backwardstri(number):
		for item in range(1, number + 1):
			backtri = ("." * item)
			print(backtri.rjust(4, " "))
	def upsidedowntri(number):
	    for item in range(number, 0, - 1):
	        print("." * item)
	triangle(4)
	print("")
	backwardstri(4)
	print("")
	upsidedowntri(4)
	print("")
triangles()

			
