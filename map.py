# CPE 101-01
# LAB 5: Map Functions
# Name: Joshua Smith
# Section: 07


# Purpose: Cube each element in a list
# Signature: list -> list
def cube_all(numbers):
    return [x ** 3 for x in numbers]


# Purpose: Add n to each element in a list
# Signature: list float -> list
def add_n_to_all(numbers, n):
    for i in range(len(numbers)):
        numbers[i] += n

    return numbers


# Purpose: Determine if each element in a list
#          is divisible by 5
# Signature: list -> list
def div_by_5_all(numbers):
    result = []

    i = 0
    while i < len(numbers):
        result.append(numbers[i] % 5 == 0)
        i += 1

    return result

