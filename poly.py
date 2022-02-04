# CPE 101-01
# LAB 5: Polynomial Functions
# Name: Joshua Smith
# Section: 07


# Purpose: Add two second-degree polynomials
# Signature: list list -> list
def poly_add2(first, second):
    return [first[0] + second[0],
            first[1] + second[1],
            first[2] + second[2]]


# Purpose: Multiply two second-degree polynomials
# Signature: list list -> list
def poly_mult2(f, s):
    # loop-based approach that I wrote before I saw that
    # I can't use loops, it's pretty so I'm saving it as
    # a comment

    # first = f
    # second = s
    # result = [0] * 5
    # for i in range(len(first)):
    #     exp1 = 2 - i
    #     for j in range(len(second)):
    #         exp2 = 2 - j

    #         result_index = 4 - (exp1 + exp2)
    #         result[result_index] += first[i] * second[j]

    # return result

    return [
        f[0] * s[0],
        f[0] * s[1] + s[0] * f[1],
        f[0] * s[2] + s[0] * f[2] + f[1] * s[1],
        f[1] * s[2] + s[1] * f[2],
        f[2] * s[2]
    ]


if __name__ == '__main__':
    print(poly_mult2([1/14, 1/7, 4.14], [1, 1, 1]))