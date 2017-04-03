def getSeat():
    row = int(input("Row Number (integer): "))
    seat = input("Seat Number (A-F): ")

    a = seat.upper()
    Seat_wanted = [row,a]
    return (Seat_wanted)

L = [['-','-']]
print(L)

def createTAble(row, seats):
    a = []
    for x in range(row):
        a[x][0] = x

    for y in range(seats):
        a[0][y] = y

    return a


def main():
    NUM_ROWS = 6
    NUM_SEATS = 5
    a = ['-', 'X']
    print("   {:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('A', 'B', 'C', 'D', 'E', 'F', 'G'))
    print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('1:', a[0], a[1], 'C', 'D', 'E', 'F'))
    print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('2:', 'A', 'B', 'C', 'D', 'E', 'F'))
    print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('3:', 'A', 'B', 'C', 'D', 'E', 'F'))
    print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('4:', 'A', 'B', 'C', 'D', 'E', 'F'))
    print("{:2} {:2} {:2} {:2} {:2} {:2} {:2}".format('5:', 'A', 'B', 'C', 'D', 'E', 'F'))
    print([[x for x in range(NUM_ROWS)], [y for y in range(NUM_SEATS)]])
    print([['-' for y in range(NUM_SEATS)] for x in range(NUM_ROWS)])
    print('asdfs')


if __name__ == "__main__":
    main()

    #hello world