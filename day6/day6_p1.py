f = open('day6_input.txt')
input = f.read().split('\n')

for i, row in enumerate(input):
    input[i] = row.split()

#transpose
input_transpose = [list(i) for i in zip(*input)]

total_array=[]
length_of_operation = len(input_transpose[0])

for column in input_transpose:
    operator = column[length_of_operation-1]
    tally=1
    
    if operator == '*':
        for j in range(0,length_of_operation-1):
            tally = int(column[j])*tally
        total_array.append(tally)

    elif operator == '+':
        tally=0
        for j in range(0,length_of_operation-1):
            tally = int(column[j])+tally
        total_array.append(tally)

print(sum(total_array))
