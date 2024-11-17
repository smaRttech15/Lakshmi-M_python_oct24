def digit_frequency(number, digit):
    return str(number).count(str(digit))

# Example usage:
num = 153553
digit = 5
print(f"Frequency of {digit} in {num}: {digit_frequency(num, digit)}")  # Output: 3