def is_alphanumeric(char):
    return char.isalnum()

# Example usage:
character = 'A1'
print(f"'{character}' is alphanumeric: {is_alphanumeric(character)}")  # Output: True

character = '@'
print(f"'{character}' is alphanumeric: {is_alphanumeric(character)}")  # Output: False