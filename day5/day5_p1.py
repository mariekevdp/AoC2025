f = open('day5_input.txt')
input = f.read().split('\n\n')

fresh_ID_ranges = input[0].split('\n')
ingredient_IDs = input[1].split('\n')

fresh_IDs_array=[]
fresh_count=0
print('total IDs to check', len(ingredient_IDs))

i=0
for ID in ingredient_IDs:
    i+=1
    print('current ID', i)
    ID_fresh_flag=0

    for ID_range in fresh_ID_ranges:
        start = int(ID_range.split('-')[0])
        end = int(ID_range.split('-')[1])

        if int(ID) >= start and int(ID) <= end:
            ID_fresh_flag=1

    if ID_fresh_flag==1:
        fresh_count+=1

print('fresh count', fresh_count)