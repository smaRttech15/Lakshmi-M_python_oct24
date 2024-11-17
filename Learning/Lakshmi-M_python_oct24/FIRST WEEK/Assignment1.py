def can_arrange(n, boys, girls):
    boys.sort()
    girls.sort()

    pattern1 = [val for pair in zip(boys, girls) for val in pair]
    pattern2 = [val for pair in zip(girls, boys) for val in pair]

    def is_non_decreasing(arr):
        return all(arr[i] <= arr[i + 1] for i in range(len(arr) - 1))

    return "YES" if is_non_decreasing(pattern1) or is_non_decreasing(pattern2) else "NO"

test_case = int(input())
results = []

for _ in range(test_case):
    n = int(input())  
    boys = list(map(int, input().split())) 
    girls = list(map(int, input().split())) 
    results.append(can_arrange(n, boys, girls))

for result in results:
    print(result)