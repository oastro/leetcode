# Count Divisibles in Range

# Dados dois números inteiros, n e k,
# a tarefa é contar quantos números entre 1 e n (inclusive)
#  são divisíveis por k.

def count_divisible(n: int, k: int) -> int:
    counter = 0
    index = 1

    while index <= n:
        if (index % k == 0):
            counter += 1
        index += 1

    return counter


print("Example:")
print(count_divisible(2, 1))

# These "asserts" are used for self-checking
assert count_divisible(10, 2) == 5
assert count_divisible(10, 3) == 3
assert count_divisible(10, 5) == 2
assert count_divisible(15, 4) == 3
assert count_divisible(20, 6) == 3
assert count_divisible(100, 10) == 10
assert count_divisible(200, 25) == 8
assert count_divisible(50, 7) == 7
assert count_divisible(60, 8) == 7
assert count_divisible(70, 9) == 7

print("The mission is done! Click 'Check Solution' to earn rewards!")
