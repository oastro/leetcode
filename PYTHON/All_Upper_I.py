# All Upper I

# Verifique se uma determinada sequência tem todos os símbolos em maiúsculas.
# Se a string estiver vazia ou não tiver nenhuma letra - a função deve retornar True.

def is_all_upper(text: str) -> bool:
    for index in text:
        if (index.islower()):
            return False

    return True


print("Example:")
print(is_all_upper("ALL UPPER"))

# These "asserts" are used for self-checking
assert is_all_upper("ALL UPPER") == True
assert is_all_upper("all lower") == False
assert is_all_upper("mixed UPPER and lower") == False
assert is_all_upper("") == True
assert is_all_upper("444") == True
assert is_all_upper("55 55 5 ") == True

print("The mission is done! Click 'Check Solution' to earn rewards!")
