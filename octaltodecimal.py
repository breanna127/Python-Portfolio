def octal_to_decimal(octal_str):
    decimal_value = 0
    exponent = len(octal_str) - 1

    for digit in octal_str:
        decimal_value += int(digit) * (8 ** exponent)
        exponent -= 1

    return decimal_value

# Example usage
octal_number = input("Enter an octal number: ")
decimal_result = octal_to_decimal(octal_number)
print(f"The decimal equivalent of octal {octal_number} is {decimal_result}")