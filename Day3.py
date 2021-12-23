print("\n\n\n")

maximum = {}
minimum = {}
for line in open("Day3.txt"):

    line = line.strip()
    for i, value in enumerate(line):
        if i not in maximum:
            maximum[i] = 0
        if i not in minimum:
            minimum[i] = 0
        if value == '1':
            maximum[i] += 1
        else:
            minimum[i] += 1

gamma = ''
epsilon = ''

for i in minimum:
    if minimum[i] > maximum[i]:
        gamma += '0'
        epsilon += '1'
    else:
        gamma += '1'
        epsilon += '0'

print(int(gamma,2) * int(epsilon,2))