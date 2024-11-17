import sys
def linear_search(my_list, key):
    for i in range(len(my_list)):
        if my_list[i] == key:
            return i
    return -1
numbers = list()
print(type(sys.argv))
for i in range(1, len(sys.argv)):
    numbers.append(float(sys.argv[i]))
print(f'User given numbers are: ', numbers)
key = float(input('Enter number to be searched: '))
position = linear_search(tuple(numbers), key)
if position == -1:
    print(f'The element {key} was not found')
else:
    print(f'The element {key} was found at position {position+1}')