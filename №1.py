def sorter(numbers): #It removes all the zeros from the list and appends them to the end of the list.
    zeros_counter = numbers.count(0)
    numbers = [x for x in numbers if x != 0]
    for i in range(zeros_counter):
        numbers.append(0)
    return numbers

def main():
    integers = [4, 0, 5, 0, 3, 0, 0, 5]
    print(sorter(integers))

if __name__ == "__main__":
    main()