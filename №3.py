def inputCoordinates():
    """
    It asks the user to input the coordinates of the start and end squares, and returns them as a tuple
    """
    startRow = int(input("Enter row of first square: "))
    startColumn = input("Enter column of first square: ")
    endRow = int(input("Enter row of second square: "))
    endColumn = int(input("Enter column of second square: "))
    return startRow, startColumn, endRow, endColumn

def checkMove(firstRow, firstColumn, secondRow, secondColumn):
    """
    If the first row is equal to the second row and the first column is not equal to the second column,
    or if the first row is not equal to the second row and the first column is equal to the second
    column, or if the difference between the first row and the second row is equal to the difference
    between the first column and the second column, then return "YES", otherwise return "NO".
    """
    if firstRow == secondRow and firstColumn != secondColumn:
        return "YES"
    elif firstRow != secondRow and firstColumn == secondColumn:
        return "YES"
    elif (firstRow - secondRow) == (firstColumn - secondColumn):
        return "YES"
    else:
        return "NO"

def main():
    startRow, startColumn, endRow, endColumn = inputCoordinates()
    print(checkMove(int(startRow), int(startColumn), int(endRow), int(endColumn)))

if __name__ == '__main__':
    main()