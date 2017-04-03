def getSeat(rows, seats):
    row = int(input("Row Number (1-{}): ".format(str(rows))))
    seat = input("Seat Number (A-{}): ".format(chr(64+seats)))
    a = ord(seat.upper()) - ord("A")
    Seat_wanted = [row-1, a]
    return (Seat_wanted)


def createTable(row, seats):
    return [[True for y in range(seats)] for x in range(row)]


def printTable(table):
    print("SEATING CHART   Available Seats: {}".format(availableSeats(table)))

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


def availableSeats(table):
    count = 0
    for row in table:
        for seat in row:
            if seat:
                count += 1
    return count

def reset(table):
    return createTable(len(table), len(table[0]))

def main():
    NUM_ROWS = 6
    NUM_SEATS = 5
    table = createTable(NUM_ROWS,NUM_SEATS)
    ###########
    while True:
        print("Flight Reservation System")
        print(" 1: Display Seat chart")
        print(" 2: Reserve a seat")
        print(" 3: Count available seats")
        print(" 4: Quit")
        print(" 5: Reset\n")
        menu = int(input("Enter your selection: "))
    ###########
        if menu == 1:
            printTable(table)
            print("\n")
    ###########
        if menu == 2:
            while True:
                row , col = getSeat(NUM_ROWS, NUM_SEATS)
                if table[row][col]:
                    table[row][col] = False
                    printTable(table)
                    break
                else:
                    print("\nThat Seat Has Already Been Takin Sorry!!!\n")
    ###########
        if menu == 3:
            print("Available Seats: {}".format(availableSeats(table)))

        if menu == 4:
            print("Exiting Program - have a nice flight")
            break

        if menu == 5:
            table = reset(table)



if __name__ == "__main__":
    main()
