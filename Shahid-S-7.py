def getSeat():
    row = int(input("Row Number (integer): "))
    seat = input("Seat Number (A-F): ")
    a = ord(seat.upper()) - ord("A")
    Seat_wanted = [row-1, a]
    return (Seat_wanted)


def createTable(row, seats):
    a = []
    a = [['-' for y in range(seats)] for x in range(row)]

    return a


def main():
    while True:
        NUM_ROWS = 6
        NUM_SEATS = 5
        table = createTable(NUM_ROWS,NUM_SEATS)
        row , col = getSeat()
        table[row][col] = 'X'
        print(table)

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
