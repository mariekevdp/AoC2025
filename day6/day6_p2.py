f = open('day6_input.txt')
input = f.read().split('\n')

input_no_operators = input
last_row = input_no_operators.pop() #pop returns the item that has been removed
op_index_array=[]

for i,char in enumerate(last_row):
    if char != ' ':
        op_index_array.append(i)

number_of_calcs = len(op_index_array) #this is 1000
total_array=[]

for calc in range(number_of_calcs):
        operator = last_row[op_index_array[calc]]

        number_section=[]
        variable_array = []

        for j,row in enumerate(input_no_operators):
            try:
                number_section.append(input_no_operators[j][op_index_array[calc]:op_index_array[calc+1]-1])
            except:#special case for last calc
                number_section.append(input_no_operators[j][op_index_array[calc]:])
        
        for i in range(len(number_section[0])): #columns
            temp_var = ''
            for k,row in enumerate(number_section): #rows
                temp_var = temp_var+number_section[k][i]
            variable_array.append(temp_var)
        

        if operator == '*':
            tally=1
            for n,variable in enumerate(variable_array):
                tally = tally*(int(variable.strip()))
            total_array.append(tally)

        elif operator == '+':
            tally=0
            for n,variable in enumerate(variable_array):
                tally = tally+(int(variable.strip()))
            total_array.append(tally)
        

print(sum(total_array))