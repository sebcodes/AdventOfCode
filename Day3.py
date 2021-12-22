# This is a sample Python script.

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

gamma = ''
epsilon = 0

# Press the green button in the gutter to run the script.
if __name__ == '__main__':

    file1 = open('Day3.txt', 'r')
    Lines = file1.readlines()
    string = ''
    split_strings = []
    strings = []
    count = 0
    # Strips the newline character
    for line in Lines:
        n = 1
        split_strings = [line[index: index + n] for index in range(0, len(line), n)]
        # Remove new line character
        if len(line) > 5:
            split_strings = split_strings[:-1]
        # print(split_strings)
        strings.append(split_strings)


def getfirsthighestbit():
    max = 0
    min = 0
    buffer = 0
    for reports in strings:
        if int(reports[0]) == 1:
            max += max
        elif int(reports[0]) == 0:
            min += min

    if min > max:
        buffer = min
    else:
        buffer = max
    print("Erstes häufigstes Bit : {} ".format(buffer))


getfirsthighestbit()