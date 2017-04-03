def getSeat():
    row = int(input("Row Number (integer): "))
    seat = input("Seat Number (A-F): ")
    a = ord(seat.upper()) - ord("A")
    Seat_wanted = [row-1, a]
    return (Seat_wanted)


def createTable(row, seats):
    return [[True for y in range(seats)] for x in range(row)]


def printTable(table):
    # two python functions for ascii
    # ord(x) and chr(x)
    # ord - finds you the ascii value
    # chr - converts ascii value into character
    rows = len(table)
    seats = len(table[0])

    firstString = ""
    for x in range(seats):
        firstString += " {:2}".format(chr(65 + x))  # 66 + 0 , 66 is b since we already added A
    print("  " + firstString)

    eachRowString = ""
    for row in range(rows):
        eachRowString += "{:2}".format(row + 1)
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
    table = createTable(NUM_ROWS,NUM_SEATS)
    while True:
        row , col = getSeat()
        if table[row][col] == True:
            table[row][col] = False
        else:
            print("\nThat Seat Has Already Been Takin Sorry!!!\n")
        printTable(table)

    # print("   {:2} {:2} {:2} {:2} {:2} {:2} ".format('A', 'B', 'C', 'D', 'E', 'F',))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('1:', 'B', 'C', 'C', 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('2:', 'A', 'B', 'C', 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('3:', 'A', 'B', table[2][2], 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('4:', 'A', 'B', 'C', 'D', 'E', 'F'))
    # print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('5:', 'A', 'B', 'C', 'D', 'E', 'F'))
    #print([[x for x in range(NUM_ROWS)], [y for y in range(NUM_SEATS)]])
    #print([['-' for y in range(NUM_SEATS)] for x in range(NUM_ROWS)])



if __name__ == "__main__":
    main()
