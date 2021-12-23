# This is a sample Python script.
import binascii

# Press Umschalt+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.

gamma = ''
epsilon = 0


def int_to_bytes(x: int) -> bytes:
    return x.to_bytes((x.bit_length() + 7) // 8, 'big')


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
        if len(line) > 12:
            split_strings = split_strings[:-1]
        # print(split_strings)
        strings.append(split_strings)


def getfirsthighestbit():
    max = 0
    min = 0
    for reports in strings:
        if int(reports[0]) == 1:
            max += 1
            # print("Max : {}".format(max))

        elif int(reports[0]) == 0:
            min += 1
            # print("Min : {}".format(min))

    if min > max:
        buffer = 0
    else:
        buffer = 1
    print("Erstes häufigstes Bit : {} ".format(buffer))


def getsecondhighestbit():
    max = 0
    min = 0
    for reports in strings:
        if int(reports[1]) == 1:
            max += 1
            # print("Max : {}".format(max))

        elif int(reports[1]) == 0:
            min += 1
            # print("Min : {}".format(min))

    if min > max:
        buffer = 0
    else:
        buffer = 1
    print("Zweites häufigstes Bit : {} ".format(buffer))


def third():
    max = 0
    min = 0
    for reports in strings:
        if int(reports[2]) == 1:
            max += 1
            # print("Max : {}".format(max))

        elif int(reports[2]) == 0:
            min += 1
            # print("Min : {}".format(min))

    if min > max:
        buffer = 0
    else:
        buffer = 1
    print("Drittes häufigstes Bit : {} ".format(buffer))


# getfirsthighestbit()
# getsecondhighestbit()
# third()

for x in range(5):
    max = 0
    min = 0
    for reports in strings:
        if int(reports[x]) == 1:
            max += 1

        elif int(reports[x]) == 0:
            min += 1

    if min >= max:
        buffer = 0
    else:
        buffer = 1
    print("{}. häufigstes Bit : {} ".format(x, buffer))
print("\n\n\n")
for x in range(5):
    max = 0
    min = 0
    for reports in strings:
        if int(reports[x]) == 1:
            max += 1

        elif int(reports[x]) == 0:
            min += 1

    if min >= max:
        buffer = 1
    else:
        buffer = 0
    print("{}. häufigstes Bit : {} ".format(x, buffer))
