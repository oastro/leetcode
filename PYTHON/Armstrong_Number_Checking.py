# Armstrong Number Checking

# Na teoria dos números, um número (após ) ou número narcisista em uma dada base numérica
# (10 para esta missão) é um número que é a soma de seus próprios dígitos,
# cada um elevado à potência do número de dígitos.
# Por exemplo, 153 é um número porque .13 + 53 + 33 == 153

def is_armstrong(num: int) -> bool:
    result = 0
    exponent = len(str(num))

    for digit in str(num):
        result += int(digit) ** exponent

    if (result == num):
        return True
    return False


print("Example:")
print(is_armstrong(11))

# These "asserts" are used for self-checking
assert is_armstrong(153) == True
assert is_armstrong(370) == True
assert is_armstrong(947) == False
assert is_armstrong(371) == True
assert is_armstrong(407) == True
assert is_armstrong(163) == False
assert is_armstrong(100) == False
assert is_armstrong(8208) == True
assert is_armstrong(930) == False
assert is_armstrong(4) == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
