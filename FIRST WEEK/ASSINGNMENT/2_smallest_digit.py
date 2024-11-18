def second_smallest_digit(number):
    digits = sorted(set(int(digit) for digit in str(number)))
    return digits[1] if len(digits) > 1 else None

num = 67834589
print(f"2nd smallest digit in {num}: {second_smallest_digit(num)}")  # Output: 4