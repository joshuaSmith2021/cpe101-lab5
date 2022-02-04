# CPE 101-01
# LAB 5: Nested Functions
# Name: Joshua Smith
# Section: 07


# Purpose: Multiply inner lists
# Signature: list -> list
def product(values):
    result = []
    for numbers in values:
        current_product = 1
        for number in numbers:
            current_product *= number

        result.append(current_product)

    return result

