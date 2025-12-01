f = open('day1_input.txt')
instructions = f.read().splitlines()

start = 50
position = start
zero_count = 0


for instruction in instructions:
    start_position = position
    if instruction.startswith('R'):
        position = position + int(''.join(instruction[1:]))

        while position > 99:
            position = position - 100 
            zero_count += 1
    else:
        position = position - int(''.join(instruction[1:]))
        
        if position == 0:
            zero_count += 1

        while position < 0:
            position = position + 100
            zero_count += 1
            if position == 0:
                zero_count += 1

        if start_position == 0:
             zero_count -= 1

            
            
print(position)
print(zero_count)