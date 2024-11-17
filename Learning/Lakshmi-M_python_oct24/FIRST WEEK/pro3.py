#small_of_two_nums
num1 = int(input('Enter the first number:'))
num2 = int(input('Enter the second number: '))

if num1 < num2:
    print('Num1 =', num1, ' is smallest')
else:
    print('Num2 = ' + str(num2) + ' is smallest')

#int_data_into_str
num2 = 235
print('Num2 = ' + str(num2) + ' is a 3 digit number')

#range()
for i in range(30, 10, -2):
	print(i)
	i -= 2