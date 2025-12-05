f = open('day5_input.txt')
input = f.read().split('\n\n')

fresh_ID_ranges = input[0].split('\n')

fresh_IDs_array=[]

i=0

for ID_range in fresh_ID_ranges:
    i+=1
    print(i)
    start = int(ID_range.split('-')[0])
    end = int(ID_range.split('-')[1])

    for i in range (start,end+1,1):
        fresh_IDs_array.append(i)

    fresh_IDs_array = list(set(fresh_IDs_array))

