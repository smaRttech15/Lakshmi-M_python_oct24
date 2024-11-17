def is_composite_number(n):
    if n < 4:
        return False
    for i in range(2, int(n**0.5) + 1):
        if n % i == 0:
            return True
    return False
digit = int(input())
print(f"{digit} is a composite number: {is_composite_number(digit)}")