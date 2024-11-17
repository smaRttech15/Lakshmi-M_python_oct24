#program 6a
import sys
numbers = [15,21,12,2]
for i in range(1, len(sys.argv)):
    numbers.append(int(sys.argv[i]))
print(numbers)
strings = [str(element) for element in numbers]
print(strings)
even_numbers = [element for element in numbers if element % 2 == 0]
print(even_numbers)

#program 6b
import sys
strings = sys.argv
print(strings)
numbers = [int(num) for num in strings if num.isnumeric()]
print(numbers)

#format_specifiers(6c)
num1 = 23
num2 = 0o23
num3 = 0xab

print('%d  %o  %x  %X'%(num1, num1, num1, num1))
print('%d  %o  %x  %X'%(num2, num2, num2, num2))
print('%d  %o  %x  %X'%(num3, num3, num3, num3))

#deletion(6d)
l1 = [2, 3, 5]
print(l1)
del l1[0]
print(l1)
del l1[0]
print(l1)
del l1[0]
print(l1)