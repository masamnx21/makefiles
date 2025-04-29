if __name__=='__main__':
	#creating output file named makefiletwo.txt
	outfile = open('makefiletwo.txt', 'w')
	
	#defining variables for math later
	x = 12
	y = 4	

	#writing output to makefiletwo.txt
	outfile.write('Hi Dr. Kruse! \nThis is the second output file. \n')
	outfile.write('This will show some simple math. \n')
	outfile.write('if x = 12 and y = 4: \n')
		
	#addition with x and y
	outfile.write('x + y = '+str(x+y)+'\n')

	#subtraction with x and y
	outfile.write('x - y = '+str(x-y)+'\n')

	#division with x and y
	outfile.write('x / y = '+str(x / y)+'\n')
