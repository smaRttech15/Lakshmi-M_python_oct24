def sum_even_odd_digits(number):
    even_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 == 0)
    odd_sum = sum(int(digit) for digit in str(number) if int(digit) % 2 != 0)
    return even_sum, odd_sum

# Example usage:
num = 12345
even_sum, odd_sum = sum_even_odd_digits(num)
print(f"Sum of even digits: {even_sum}, Sum of odd digits: {odd_sum}")  # Output: 6, 9