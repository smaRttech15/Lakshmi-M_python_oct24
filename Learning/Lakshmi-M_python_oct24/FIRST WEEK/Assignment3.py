n = int(input())
arr1 = list(map(int, input().split()))

m = int(input())
arr2 = list(map(int, input().split()))

freq1 = {}
freq2 = {}

for num in arr1:
    freq1[num] = freq1.get(num, 0) + 1

for num in arr2:
    freq2[num] = freq2.get(num, 0) + 1

missing_numbers = []
for num in freq2:
    if freq2[num] > freq1.get(num, 0):  
        missing_numbers.append(num)
missing_numbers.sort()
print(" ".join(map(str, missing_numbers)))