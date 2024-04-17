import pandas as pd

# location of text file to sort
file_location = 'C://Users//reedb//Desktop//Notes//Passwords.txt'

# desired location of sorted text file
file_destination = 'C://Users//reedb//Desktop//sorted_passwords.txt'

#opening file and splittiing file into lines
with open(file_location, 'r') as f:
    lines = f.read().split('\n')

#creating a list for each entry
new_list=[[]]
list_index = 0
for i in range(len(lines)):
    if lines[i] != '':
        new_list[list_index].append(lines[i])
    else:
        new_list.append([])
        list_index += 1

# getting max length of sublists
max_length = 0
for item in new_list:
    if len(item) > max_length:
        max_length = len(item)

# creating list of needed columns for DataFrame
if max_length < 3:
        raise Exception('Entries should have 3 fields: name, user, and password.')
elif max_length > 3:
    col_list = ['name', 'user', 'pass']
    for i in range(4, max_length + 1):
        col_list.append(str(i))

# loading into a DataFrame to sort by name
df = pd.DataFrame(new_list, columns = col_list)
df = df.set_index('name')
df = df.sort_values('name')

df.replace(to_replace=[None], value=0, inplace=True)

# name is now index, so it is not needed in col_list
col_list.remove('name')

# writing sorted file into a new text file
with open(file_destination, 'w') as f:
    for index, row in df.iterrows():
        f.write(index)
        f.write('\n')
        for item in [row[x] for x in col_list]:
            if item != 0:
                f.write(item)
                f.write('\n')
        f.write('\n')

print('Success!')
print('Sorted password file created at address', file_destination)



