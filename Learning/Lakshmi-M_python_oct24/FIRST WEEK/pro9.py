#9a
my_str = 'banashankari'
sub_string = 'm'
try:
    print(my_str.index('s')) # 4
    print(my_str.index(sub_string)) # error
    print(my_str.index('shankari')) 
except ValueError as e:
    print(f'The sub string {sub_string} not found')
    print(e.__str__())
except:
    print('Some error occured')
#9b
numbers1 = []
numbers2 = list()
numbers3 = [1, 2, 3, 4, 5]
numbers4 = list(numbers3)
numbers5 = list(numbers3[1:4])
print(numbers1)
print(numbers2)
print(numbers3)
print(numbers4)
print(numbers5)
#9c
input_size = int(input('Enter size of the Array: '))
numbers = []
for i in range(input_size):
    number = int(input())
    numbers.append(number)
    # numbers.append(int(input()))
print('The array is: ', numbers)
print(f'The array of size {input_size} is:')
for number in numbers:
    print(number, end='  ')
#9d
print('Enter space seperated numbers in a line')
user_input = input()
print(type(user_input))
numbers = [int(number) for number in user_input.split()]
print('The array is: ', numbers)
#9e
list1 = [2, 3, 5, 7, 11, 13]

list2 = list1[3:] # creates a new list
list2[2] = 100
print(list1)
print(list2)