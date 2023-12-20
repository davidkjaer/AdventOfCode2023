with open("input.txt", "r") as input:
    sum = 0
    names = {"one": "1", "two": "2", "three": "3", "four": "4", "five": "5",
             "six": "6", "seven": "7", "eight": "8", "nine": "9"}
    for line in input.readlines():
        line = line.strip()
        # Find first match of a key in names in line
        digits = []
        at = 0
        while at < len(line):
            for x in names.keys():
                if line[at].isdigit():
                    digits.append(int(line[at]))
                elif line[at:].startswith(x):
                    digits.append(int(names[x]))
                    break
            at = at + 1

        #print(line)
        # filter all digits out of line
        sum += 10 * digits[0] + digits[-1]
    print(sum)