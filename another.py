"#python" 
def getSeat():
    pass


def createTable(rows, seats):
	#creating a table with the values of rows and seats from the parameter
	#using two for loops
	# for loop ->   x for x in range(someValue) is similar to 
	# for x in range(someValue):
	#	x
	return [[False for y in range(seats)] for x in range(rows)]

def printTable(table):
	# two python functions for ascii 
	# ord(x) and chr(x)
	# ord - finds you the ascii value
	# chr - converts ascii value into character 
	rows = len(table)
	seats = len(table[0])

	firstString = ""
	for x in range(seats):
		firstString += " {:2}".format(chr(65+x))  # 66 + 0 , 66 is b since we already added A 
	print("  "+firstString)

	eachRowString = ""
	for row in range(rows):
		eachRowString += "{:2}".format(row+1)
		for seat in range(seats):
			if table[row][seat]:
				eachRowString += " {:2}".format('-')
			else:
				eachRowString += " {:2}".format('x')

		print(eachRowString)
		eachRowString = ""



def main():
    NUM_ROWS = 6
    NUM_SEATS = 5

    table = createTable(NUM_ROWS, NUM_SEATS)
    printTable(table)



    # a = ['-', 'X']
    # print("   {:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('A', 'B', 'C', 'D', 'E', 'F', 'G'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('1:', a[0], a[1], 'C', 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('2:', 'A', 'B', 'C', 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('3:', 'A', 'B', 'C', 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('4:', 'A', 'B', 'C', 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('5:', 'A', 'B', 'C', 'D', 'E', 'F'))
    # print([[x for x in range(NUM_ROWS)], [y for y in range(NUM_SEATS)]])
    # print([['-' for y in range(NUM_SEATS)] for x in range(NUM_ROWS)])
    # print('asdfs')


if __name__ == "__main__":
    main()

    #hello world