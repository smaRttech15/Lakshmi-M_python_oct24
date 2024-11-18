n = int(input()) 
oranges = list(map(int, input().split())) 

k = 0  

for i in range(n - 1):
    if oranges[i] <= oranges[n - 1]:
        oranges[i], oranges[k] = oranges[k], oranges[i]
        k += 1

oranges[k], oranges[n-1] = oranges[n-1], oranges[k]

print(" ".join(map(str, oranges)))