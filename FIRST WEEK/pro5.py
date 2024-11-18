numbers = [3, 7, 19, 11, 13, 5, 17] #5a

print(numbers)
print(numbers.count(7))
print(numbers.count(27))
numbers.reverse()
print(numbers)
print(sorted(numbers)) #print(numbers.sort())

list1  = [29, 23, 19, 11, 13, 5, 17, 37] #5b
list2 = [3, 7, 31, 2]
list3 = [43, 41, 47]
l1 = [1 ,2 ,3]
l2 = [1 ,2 ,3]
print(list1 + list2)
print(list2 > list1)
list1.extend(list2)
print(list1)
list2.insert(2, list3)
print(list2)
print(l1.__eq__(l2))
l1.append(input())
l2.append(input())
print(l1 == l2)

#swap 2 numbers(5c)
x = [5, 10]
y = [9, 3]
print('Before Swapping:\n X =', x, 'Y =', y)
x, y = y, x
print('After swapping:\n X =', x, 'Y =', y)

#split_join_operation(5d)
names = input().split(',')
print(names)
new_names = ' '.join(names)
print(new_names)
names = [input('Enter space seperated names: ').split()]
print(names)