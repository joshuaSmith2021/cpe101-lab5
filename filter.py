# CPE 101-01
# LAB 5: Filter Functions
# Name: Joshua Smith
# Section: 07


# Purpose: Find even numbers in list
# Signature: list -> list
def are_even(numbers):
    return [x for x in numbers if x % 2 == 0]


# Purpose: Remove duplicates from a list
# Signature: list -> list
def remove_duplicates(values):
    result = []
    for value in values:
        if value not in result:
            result.append(value)

    return result


# Purpose: Test if numbers are divisible by n
# Signature: list int -> list
def are_divisible_by_n(numbers, n):
    result = []

    i = 0
    while i < len(numbers):
        if (current := numbers[i]) % n == 0:
            result.append(current)

        i += 1

    return result


if __name__ == '__main__':
    test = list(range(60)) * 2
    print(remove_duplicates(test))
