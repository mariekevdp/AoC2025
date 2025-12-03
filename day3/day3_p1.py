f = open('day3_input.txt')
batterybank_list = f.read().split('\n')

max_joltage_list = []

for batterybank in batterybank_list:

    char1 = max(batterybank)

    index = batterybank.index(max(batterybank))

    if index == len(batterybank)-1:
        char2 = char1
        char1 = max(batterybank[:len(batterybank)-1])

    else:
        char2 = max(batterybank[index+1:])

    max_joltage_list.append(int(''.join(char1+char2)))


print(sum(max_joltage_list))








