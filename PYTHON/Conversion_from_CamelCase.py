# Conversion from CamelCase

# Sua missão é converter o nome de uma função do CamelCase ("MyFunctionName")
# para o formato Python ("my_function_name"), onde todos os caracteres estão em minúsculas
# e todas as palavras são concatenadas com um símbolo de sublinhado intermediário "_".

def from_camel_case(name: str) -> str:
    result = ''

    for index, char in enumerate(name):
        if (char.isupper() and index != 0):
            result += '_' + char
        else:
            result += char

    return result.lower()


print("Example:")
print(from_camel_case("MyFunctionName"))

# These "asserts" are used for self-checking
assert from_camel_case("MyFunctionName") == "my_function_name"
assert from_camel_case("IPhone") == "i_phone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
