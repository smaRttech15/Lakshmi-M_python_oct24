def sum_of_digits(number):
    return sum(int(digit) for digit in str(number))

# Example usage:
num = 1521
print(f"Sum of digits in {num}: {sum_of_digits(num)}") #output 9