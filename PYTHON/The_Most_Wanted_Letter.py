# The Most Wanted Letter

# Dado um texto que contém várias letras em inglês e sinais de pontuação.
# Você deve encontrar a letra mais frequente no texto.
# A letra retornada deve ser uma letra minúscula.
# Ao procurar a letra mais frequente,
# diferenças entre maiúsculas e minusculas não importam,
# de modo que para a busca assuma que "A" == "a".
# Certifique-se de não considerar pontuação, números e espaços em branco na busca, apenas letras.
# Se o texto possui duas ou mais letras com a mesma frequência,
# então o resultado será a letra que vem primeiro no alfabeto latino.
# Por exemplo -- "one" contém "o", "n", "e" apenas uma vez para cada um, de modo que nós escolhemos "e".

def checkio(text: str) -> str:
    array = list(text.lower())
    counter = {}

    for index in array:
        if index.isalpha():
            if index in counter:
                counter[index] += 1
            else:
                counter[index] = 1

    accountantOrder = sorted(counter)

    return max(accountantOrder, key=counter.get)


print("Example:")
print(checkio("Hello World!"))

# These "asserts" are used for self-checking
assert checkio("Hello World!") == "l"
assert checkio("How do you do?") == "o"
assert checkio("One") == "e"
assert checkio("Oops!") == "o"
assert checkio("AAaooo!!!!") == "a"
assert checkio("abe") == "a"

print("The mission is done! Click 'Check Solution' to earn rewards!")
