f = open('day2_input.txt')
product_IDs = f.read().split(',')

invalid_IDs = []

for product_ID in product_IDs:
    x = product_ID.find('-')
    firstID = int(''.join(product_ID[:x]))
    lastID = int(''.join(product_ID[x+1:]))

    for ID in range(firstID,lastID+1,1):
        IDstr = str(ID)
        string_length = len(IDstr)

        if string_length % 2 == 0: #must be even
            if (IDstr[:int(string_length/2)]) == (IDstr[int(string_length/2):]):
                invalid_IDs.append(ID)
                print('invalid ID found', ID)

print(sum(invalid_IDs))