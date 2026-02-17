# Digits Multiplication

# Você recebe um número positivo.
# Sua função deve calcular o produto dos dígitos
#  excluindo quaisquer zeros.
# Por exemplo:
#   O número dado é 123405.
#   O resultado será 1*2*3*4*5=120
#   (não esqueça de excluir zeros).

def checkio(number: int) -> int:
    counter = 1

    for index in str(number):
        if (int(index) != 0):
            counter *= int(index)

    return counter


print("Example:")
print(checkio(123405))

# These "asserts" are used for self-checking
assert checkio(123405) == 120
assert checkio(999) == 729
assert checkio(1000) == 1
assert checkio(1111) == 1

print("The mission is done! Click 'Check Solution' to earn rewards!")
