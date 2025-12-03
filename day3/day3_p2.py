f = open('day3_input.txt')
batterybank_list = f.read().split('\n')

max_joltage_list = []


for batterybank in batterybank_list:
    joltarray = []

    first_allowed_index = 0
    
    print(batterybank)
    for i in range(12):
        final_allowed_index = len(batterybank)-(11-i)
        print(i, first_allowed_index, final_allowed_index)

        current_max = max(batterybank[first_allowed_index:final_allowed_index])

        joltarray.append(current_max)

        first_allowed_index += batterybank[first_allowed_index:final_allowed_index].index(current_max)+1   

    print(joltarray)
    print(int(''.join(joltarray)))

    max_joltage_list.append(int(''.join(joltarray)))


print(sum(max_joltage_list))








