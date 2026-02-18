# Cut Sentence

# Sua tarefa nesta missão é encurtar uma frase
# para um comprimento que não exceda um dado número de caracteres.

# Se a frase já for curta o suficiente, você não precisa fazer nada a respeito.
# Mas se precisar ser truncado, a omissão deve ser indicada concatenando uma elipse("...") ao final da frase abreviada.

# A frase abreviada pode conter palavras e espaços completos.
# Não deve conter palavras truncadas nem espaços finais.
# A elipse foi levada em conta para o número permitido de caracteres, então não conta para o comprimento dado.

def cut_sentence(line: str, length: int) -> str:
    if (len(line) <= length):
        return line

    truncated = line[:length]

    if (length < len(line) and line[length] == ' '):
        return truncated + '...'

    lastSpace = truncated.rfind(' ')

    if (lastSpace != -1):
        truncated = truncated[:lastSpace]
        return truncated + '...'
    else:
        return '...'


print("Example:")
print(cut_sentence("Hi my name is Alex", 4))

# These "asserts" are used for self-checking
assert cut_sentence("Hi my name is Alex", 8) == "Hi my..."
assert cut_sentence("Hi my name is Alex", 4) == "Hi..."
assert cut_sentence("Hi my name is Alex", 20) == "Hi my name is Alex"
assert cut_sentence("Hi my name is Alex", 18) == "Hi my name is Alex"

print("The mission is done! Click 'Check Solution' to earn rewards!")
