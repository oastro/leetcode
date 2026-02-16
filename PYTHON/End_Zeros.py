# End Zeros

# Tente descobrir quantos zeros um número tem no final.

def end_zeros(a: int) -> int:
    numbers = str(a)[::-1]
    array = list(numbers)
    counter = 0

    for elements in array:
        if (int(elements) != 0):
            break
        elif (int(elements) == 0):
            counter += 1

    return counter


print("Example:")
print(end_zeros(10))

# These "asserts" are used for self-checking
assert end_zeros(0) == 1
assert end_zeros(1) == 0
assert end_zeros(10) == 1
assert end_zeros(101) == 0
assert end_zeros(245) == 0
assert end_zeros(100100) == 2

print("The mission is done! Click 'Check Solution' to earn rewards!")
