def sum_odd_placed_even_digits(number):
    return sum(int(digit) for index, digit in enumerate(str(number)) if (index % 2 == 0) and (int(digit) % 2 == 0))

num = 246813
print(f"Sum of odd placed even digits in {num}: {sum_odd_placed_even_digits(num)}")  # Output: 8