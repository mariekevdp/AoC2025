f = open('day2_input.txt')
product_IDs = f.read().split(',')

invalid_IDs = []

for product_ID in product_IDs:

    x = product_ID.find('-')
    firstID = int(''.join(product_ID[:x]))
    lastID = int(''.join(product_ID[x+1:]))

    for ID in range(firstID,lastID+1,1):
        invalid_flag=0
        IDstr = str(ID)
        string_length = len(IDstr)

        for i in range(string_length+1):
            divisor=i+1

            if string_length % divisor == 0 and divisor <= string_length/2:
                substring_array = []
                no_of_substrings = int(string_length/divisor)

                for index_of_substring in range(no_of_substrings):
                    start_index = (index_of_substring*divisor)
                    end_index = (index_of_substring*divisor)+divisor
                    substring_array.append(IDstr[start_index:end_index])
                    
                if len(set(substring_array)) == 1:
                    invalid_flag = 1
                    
        if invalid_flag == 1:
            invalid_IDs.append(ID)


print(sum(invalid_IDs))