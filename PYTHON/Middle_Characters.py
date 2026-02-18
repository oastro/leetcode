# Middle Characters

# Você recebe uma string onde precisa encontrar o(s) caractere(s) do meio.
# A sequência pode conter uma palavra, alguns símbolos ou uma frase inteira.
# Se o comprimento da sequência for par, então você deve devolver dois caracteres do meio, mas se o comprimento for ímpar, retorne apenas um. Para mais detalhes, veja o Exemplo.

def middle(text: str) -> str:
    array = list(text)

    if not (len(text) % 2 == 0):
        middle = len(text) // 2
        return array[middle]
    else:
        middle = len(text) // 2
        return array[middle - 1] + array[middle]


print("Example:")
print(middle("example"))

# These "asserts" are used for self-checking
assert middle("example") == "m"
assert middle("test") == "es"

print("The mission is done! Click 'Check Solution' to earn rewards!")
