def aksLines():
    linesCount = int(input("How many lines will there be? "))
    return linesCount

def inputPoem(n:int):
    """
    It takes an integer as an argument and asks the user to input a poem line by line. 
    It then counts the number of vowels and consonants in each line and prints the result. 
    It also returns the total number of vowels and consonants in the poem.
    """
    print("Enter the poem in English letters only.")
    listOfVowels = ["A", "E", "I", "O", "U", "Y"]
    vowels = 0
    consonants = 0
    for i in range(n):
        line = input(f'Input {i+1} line of poem: ')
        vowelsInLine = 0
        consonantsInLine = 0
        for p in range(len(line)):
            if line[p].upper() in listOfVowels:
                vowels += 1
                vowelsInLine += 1
            elif line[p].isalpha():
                consonants += 1
                consonantsInLine += 1
        print(
            "\nIn this line:\n"
            f'Number of vowels is {vowelsInLine}.\n'
            f'Number of consonants is {consonantsInLine}.\n'
        )
    return vowels, consonants

def main():
    linesCount = aksLines()
    vowelsCount, consonantsCount = inputPoem(linesCount)
    print("Number of vowels in entire poem:", vowelsCount)
    print("Number of consonants in entire poem:", consonantsCount)

if __name__ == '__main__':
    main()
