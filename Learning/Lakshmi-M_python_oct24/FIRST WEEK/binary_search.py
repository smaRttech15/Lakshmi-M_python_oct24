import sys
def binary_search(my_list, key):
    low = 0
    high = len(my_list)-1
    while low <= high: 
        mid = (low + high) // 2
        if key == my_list[mid]:
            return mid
        elif key < my_list[mid]:
            high = mid - 1
        else:
            low = mid + 1
    return -1
numbers = list()
print(type(sys.argv))
for i in range(1, len(sys.argv)):
    numbers.append(float(sys.argv[i]))
key = float(input('Enter number to be searched: '))
numbers.sort()
print(f'User given numbers are: ', numbers)
position = binary_search(tuple(numbers), key)
if position == -1:
    print(f'The element {key} was not found')
else:
    print(f'The element {key} was found at position {position+1}')