def decimal_to_octal(decimal_num):
    if decimal_num == 0:
        return "0"

    octal_digits: list[str] = []
    while decimal_num > 0:
        remainder = decimal_num % 8
        octal_digits.insert(0, str(remainder))
        decimal_num //= 8

    return ''.join(octal_digits)

# Example usage
decimal_number = int(input("Enter a decimal number: "))
octal_result = decimal_to_octal(decimal_number)
print(f"The octal equivalent of decimal {decimal_number} is {octal_result}")