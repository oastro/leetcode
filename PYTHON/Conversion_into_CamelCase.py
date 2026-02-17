# Conversion into CamelCase

# Sua missão é converter o nome de uma função do formato Python
# (por exemplo, "my_function_name") para CamelCase ("MyFunctionName"),
# onde o primeiro caractere de cada palavra está em maiúsculas
# e todas as palavras são concatenadas sem nenhum caractere.

def to_camel_case(name: str) -> str:
    result = []
    upperNext = True

    for char in name:
        if char == '_':
            upperNext = True
        elif upperNext:
            result.append(char.upper())
            upperNext = False
        else:
            result.append(char)

    return ''.join(result)


print("Example:")
print(to_camel_case("my_function_name"))

# These "asserts" are used for self-checking
assert to_camel_case("my_function_name") == "MyFunctionName"
assert to_camel_case("i_phone") == "IPhone"

print("The mission is done! Click 'Check Solution' to earn rewards!")
