import sys

def merge(left_array,right_array):
    i=0
    j=0
    sorted_array =[]
    while i < len(left_array) and j < len(right_array):
        if left_array[i] < right_array[j]:
            sorted_array.append(left_array[i])
            i += 1
        else:
            sorted_array.append(right_array[j])
            j +=1
    sorted_array.extend(left_array[i:])
    sorted_array.extend(right_array[j:])
    return sorted_array

def merge_Sort(numbers):
    if len(numbers) <= 1:
        return numbers
    mid = len(numbers) // 2
    left_array = merge_Sort (numbers[:mid])
    right_array = merge_Sort (numbers[mid:])
    return merge(left_array,right_array)


input_numbers = [int(number) for number in sys.argv[1:]]
print(f'user given numbers are :{input_numbers}')
sorted_numbers = merge_Sort(input_numbers)
print(f'sorted numbers are: {sorted_numbers}')