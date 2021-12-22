# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
depth = 0
horizontal = 0
aim = 0


# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file1 = open('day2.txt', 'r')
    Lines = file1.readlines()

    count = 0
    # Strips the newline character
    for line in Lines:
        name, number = line.split()
        print("Name {} Nummer {}".format(name, int(number)))
        if name == 'forward':
            horizontal += int(number)
            depth += aim * int(number)
        elif name == 'down':
            aim += int(number)
        elif name == 'up':
            aim -= int(number)

    print("Result: {} : Depth : {}".format(horizontal, depth))
    print("Result: {} ".format(horizontal * depth))
