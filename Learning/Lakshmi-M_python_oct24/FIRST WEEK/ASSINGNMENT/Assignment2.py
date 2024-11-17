#Find sum of the series: n + n2 + n3 + upto 10 terms
def sum_of_series_n(n):
    return sum(n**i for i in range(1, 11))
n = int(input())
print(f"Sum of the series for n={n}: {sum_of_series_n(n)}")

#Find sum of the series:1 - n + n2 - n3 + upto M terms
def sum_of_alternating_series(n, m):
    return sum((-1)**i * n**i for i in range(m))
n = int(input())
m = int(input())
print(f"Sum of the series for n={n} and m={m}: {sum_of_alternating_series(n, m)}") 

#Find sum of the series:1 - n/3 + n2/5 - n4/7 + n8/9 ....(1<n<5 and 1<m<10)
def sum_of_custom_series(n, m):
    return sum((-1)**i * (n**i) / (2*i + 1) for i in range(m))
# Example usage:
n = int(input())
m = int(input())
print(f"Sum of the series for n={n} and m={m}: {sum_of_custom_series(n, m)}")

#Print the Nth Prime number
def nth_prime(n):
    count = 0
    num = 1
    while count < n:
        num += 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                break
        else:
            count += 1
    return num
n = int(input())
print(f"The {n}th prime number is: {nth_prime(n)}")

#Check if the sum of Prime digits in a number is a Prime number
def is_prime(num):
    if num < 2:
        return False
    for i in range(2, int(num**0.5) + 1):
        if num % i == 0:
            return False
    return True
def sum_of_prime_digits(number):
    prime_digits = [int(d) for d in str(number) if d in '2357']
    digit_sum = sum(prime_digits)
    return digit_sum, is_prime(digit_sum)
number = int(input())
digit_sum, is_digit_sum_prime = sum_of_prime_digits(number)
print(f"Sum of prime digits in {number}: {digit_sum}, Is it prime? {is_digit_sum_prime}") 

#Print Nth term of the following series:1 2 2 3 3 5 5 7 8 11 13 13
def nth_term_series(n):
    series = []
    a, b = 1, 2
    for _ in range(n):
        if len(series) < 2 or series[-1] != b:
            series.append(b)
        a, b = b, a + b if len(series) % 2 == 0 else a + 1
    return series[n - 1]
n = int(input())
print(f"The {n}th term of the series is: {nth_term_series(n)}")

#Find sum of Even Placed Odd Digits in a number
def sum_even_placed_odd_digits(number):
    num_str = str(abs(number))
    reversed_num_str = num_str[::-1]
    sum_even_placed_odds = 0
    for index, digit in enumerate(reversed_num_str):
        digit = int(digit)
        if (index % 2 == 1) and (digit % 2 == 1):
            sum_even_placed_odds += digit        
    return sum_even_placed_odds
number = 123456789
result = sum_even_placed_odd_digits(number)
print(f"Sum of even-placed odd digits in {number}: {result}")


# Find sum of the series:n - n2/3 + n4/5 - n8/7 .....(1<n<5 and 1<m<10)
n = int(input('Enter the N value: '))
m = int(input('Enter numbers of terms in the series: '))
if (n <= 1 or n >= 5) and (m <= 1 or m >= 10):
    print('Invalid data entered')
    exit('End of Program')
sum = 0
for i in range(m):
    sum += (n ** 2 ** i) / (2 * i + 1) * ((-1) ** i)
    print('sum = ', sum, 'i = ', i)
print('Sum of the terms is ', sum)