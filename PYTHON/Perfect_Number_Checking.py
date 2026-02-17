# Perfect Number Checking

# Um número perfeito é um inteiro positivo
#   igual à soma de seus divisores próprios, excluindo-se.
# Por exemplo, 28 é um número perfeito porque
#   seus divisores são 1, 2, 4, 7 e 14, e sua soma é 28.

def is_perfect(n: int) -> bool:
    dividers = []
    result = 0

    for index in range(1, n):
        if n % index == 0:
            dividers.append(index)

    for index in dividers:
        result += index

    return (n == result)


print("Example:")
print(is_perfect(3))

# These "asserts" are used for self-checking
assert is_perfect(6) == True
assert is_perfect(2) == False
assert is_perfect(28) == True
assert is_perfect(20) == False
assert is_perfect(496) == True
assert is_perfect(30) == False
assert is_perfect(8128) == True
assert is_perfect(100) == False
assert is_perfect(500) == False
assert is_perfect(1000) == False

print("The mission is done! Click 'Check Solution' to earn rewards!")
