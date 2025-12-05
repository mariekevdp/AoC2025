f = open('day5_input.txt')
input = f.read().split('\n\n')

fresh_ID_ranges = input[0].split('\n')
ID_ranges_edit = fresh_ID_ranges

x = (len(fresh_ID_ranges))
y = 0

while x > y:
    x = len(fresh_ID_ranges)
    for ID_range in fresh_ID_ranges:

        start = int(ID_range.split('-')[0])
        end = int(ID_range.split('-')[1])

        overlap_flag=0

        for ID_compare in ID_ranges_edit:

            if ID_range != ID_compare:

                start_ref = int(ID_compare.split('-')[0])
                end_ref = int(ID_compare.split('-')[1])

                if start >= start_ref and start <= end_ref:
                    start = start_ref
                    overlap_flag=1

                if end >= start_ref and end <= end_ref:
                    end = end_ref
                    overlap_flag=1
                
                if overlap_flag==1:
                    new_range = '-'.join([str(start),str(end)])
                    try:
                        ID_ranges_edit[ID_ranges_edit.index(ID_range)]=new_range
                        ID_ranges_edit = list(set(ID_ranges_edit))
                    except:
                        pass
                    
        y = len(ID_ranges_edit)
        fresh_ID_ranges = ID_ranges_edit

total_valid_IDs=0
for range in fresh_ID_ranges:
    start = int(range.split('-')[0])
    end = int(range.split('-')[1])
    total_valid_IDs += (end-start)+1

print(total_valid_IDs)
