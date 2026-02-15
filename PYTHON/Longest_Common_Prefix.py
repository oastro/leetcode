# Longest Common Prefix

# Essa função deve pegar uma lista de cadeias ✓
# e determinar o prefixo comum mais longo entre todas as cadeias. ✓
# Se não houver prefixo comum, ✓
# ele deve retornar uma string vazia. ✓

def longest_prefix(arr: list[str]) -> str:
    if not arr:
        return ""
    
    prefix = arr[0]

    for string in arr[1:]:
        while not string.startswith(prefix):
            prefix = prefix[:-1]
            if not prefix:
                return ""
            
    return prefix

print("Example:")
print(repr(longest_prefix(["flower", "flow", "flight"])))

# These "asserts" are used for self-checking
assert longest_prefix(["flower", "flow", "flight"]) == "fl"
assert longest_prefix(["dog", "racecar", "car"]) == ""
assert longest_prefix(["apple", "application", "appetizer"]) == "app"
assert longest_prefix(["a"]) == "a"
assert longest_prefix(["", "b"]) == ""
assert longest_prefix(["same", "same", "same"]) == "same"
assert longest_prefix(["mismatch", "mister", "miss"]) == "mis"
assert longest_prefix(["alphabet", "alpha", "alphadog"]) == "alpha"
assert longest_prefix(["book", "boot", "booster"]) == "boo"
assert longest_prefix(["short", "shore", "shot"]) == "sho"

print("The mission is done! Click 'Check Solution' to earn rewards!")
