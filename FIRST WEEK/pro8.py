#Print the Math tabl of a number for multiples upto 20

input_number = int(input('Enter a number to print its Math table: '))
for i in range(1, 21):
    #print(input_number, '*', i, '=', input_number * i)
    print('%2d * %02d = %03d'%(input_number, i, input_number*i))

#Find the biggest of 3 distinct number
input_num1 = int(input('Enter 1st number: '))
input_num2 = int(input('Enter 2nd number: '))
input_num3 = int(input('Enter 3rd number: '))
if input_num1 > input_num2 and input_num1 > input_num3:
    print(f'Num1 = {input_num1} is the biggest number')
elif input_num2 > input_num3:
    print(f'Num2 = {input_num2} is the biggest number')
else:
    print(f'Num3 = {input_num3} is the biggest number')