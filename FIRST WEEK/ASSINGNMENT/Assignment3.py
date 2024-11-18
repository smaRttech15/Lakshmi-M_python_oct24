# Check if a number is a Palindrome
def is_palindrome(num):
    str_num = str(num)
    return str_num == str_num[::-1]
number = 121
if is_palindrome(number):
    print(f"{number} is a palindrome!")
else:
    print(f"{number} is not a palindrome.")


# Find sum of 1st and last digits of a number
def sum_of_first_and_last_digits(num):
    num = abs(num)
    last_digit = num % 10
    while num >= 10:
        num //= 10
    first_digit = num
    return first_digit + last_digit
number = 12345
result = sum_of_first_and_last_digits(number)
print(f"The sum of the first and last digits of {number} is {result}.")


# Print Nth digit of a number (starting from Left)
def nth_digit_from_left(num, n):
    num_str = str(abs(num))  # Convert to string to handle digits
    if n > len(num_str) or n <= 0:
        return "Invalid digit position"
    return int(num_str[n - 1])
# Example usage
number = 123456
position = 3
print(f"The {position}rd digit from the left is {nth_digit_from_left(number, position)}.")


# Print Nth digit of a number (starting from Right)
def nth_digit_from_right(num, n):
    num_str = str(abs(num))
    if n > len(num_str) or n <= 0:
        return "Invalid digit position"
    return int(num_str[-n])
# Example usage
number = 123456
position = 2
print(f"The {position}nd digit from the right is {nth_digit_from_right(number, position)}.")


# Accpet the number of Lines from the user and print the following shapes:

# 1.Right Angled Triangle
def right_angled_triangle(lines):
    for i in range(1, lines + 1):
        print('*' * i)
right_angled_triangle(5)

# 2.Equilateral Triangle
def equilateral_triangle(lines):
    for i in range(1, lines + 1):
        print(' ' * (lines - i) + '*' * (2 * i - 1))
equilateral_triangle(5)

# 3.Square
def square(lines):
    for _ in range(lines):
        print('*' * lines)
square(5)

# 4.Empty Square
def empty_square(lines):
    for i in range(lines):
        if i == 0 or i == lines - 1:
            print('*' * lines)
        else:
            print('*' + ' ' * (lines - 2) + '*')
empty_square(5)

# 5.Empty Equilateral Triangle
def empty_equilateral_triangle(lines):
    for i in range(1, lines + 1):
        if i == 1:
            print(' ' * (lines - i) + '*')
        elif i == lines:
            print('*' * (2 * i - 1))
        else:
            print(' ' * (lines - i) + '*' + ' ' * (2 * i - 3) + '*')
empty_equilateral_triangle(5)

# 6.Empty Rhombus
def empty_rhombus(lines):
    for i in range(1, lines + 1):
        print(' ' * (lines - i) + '*' + ' ' * (lines - 1) + '*')
empty_rhombus(5)

# 7.Hexagon
def hexagon(lines):
    for i in range(1, lines + 1):
        print(' ' * (lines - i) + '*' * (2 * i - 1))
    for i in range(lines - 1, 0, -1):
        print(' ' * (lines - i) + '*' * (2 * i - 1))
hexagon(5)

# 8.X shape
def x_shape(lines):
    for i in range(lines):
        for j in range(lines):
            if i == j or i + j == lines - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
x_shape(5)

# 9.X shape inside Empty Square
def x_shape_inside_empty_square(lines):
    for i in range(lines):
        for j in range(lines):
            if i == 0 or i == lines - 1 or j == 0 or j == lines - 1 or i == j or i + j == lines - 1:
                print('*', end='')
            else:
                print(' ', end='')
        print()
x_shape_inside_empty_square(7)

# 10.Pascal Triangle
def pascal_triangle(lines):
    for i in range(lines):
        coef = 1
        print(' ' * (lines - i), end='')
        for j in range(i + 1):
            print(coef, end=' ')
            coef = coef * (i - j) // (j + 1)
        print()
pascal_triangle(5)