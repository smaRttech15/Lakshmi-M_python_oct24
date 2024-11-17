def biggest_smallest_digit(number):
    digits = [int(digit) for digit in str(number)]
    return max(digits), min(digits)

# Example usage:
num = 152197
biggest, smallest = biggest_smallest_digit(num)
print(f"Biggest digit: {biggest}, Smallest digit: {smallest}")  # Output: 9, 1