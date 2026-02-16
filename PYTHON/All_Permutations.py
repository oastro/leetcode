# All Permutations

# Dada uma string, retorne todas as possíveis permutações de seus caracteres, ordenadas alfabeticamente.

from collections.abc import Iterable


def string_permutations(s: str) -> Iterable[str]:
    if (len(s) == 1):
        return [s]

    result = []

    for index, char in enumerate(s):

        rest = s[:index] + s[index+1:]
        for perm in string_permutations(rest):
            result.append(char + perm)

    return sorted(result, key=lambda x: (x[0], x))


print("Example:")
print(list(string_permutations("ab")))

# These "asserts" are used for self-checking
assert list(string_permutations("ab")) == ["ab", "ba"]
assert list(string_permutations("abc")) == [
    "abc", "acb", "bac", "bca", "cab", "cba"]
assert list(string_permutations("a")) == ["a"]
assert list(string_permutations("abcd")) == [
    "abcd",
    "abdc",
    "acbd",
    "acdb",
    "adbc",
    "adcb",
    "bacd",
    "badc",
    "bcad",
    "bcda",
    "bdac",
    "bdca",
    "cabd",
    "cadb",
    "cbad",
    "cbda",
    "cdab",
    "cdba",
    "dabc",
    "dacb",
    "dbac",
    "dbca",
    "dcab",
    "dcba",
]

print("The mission is done! Click 'Check Solution' to earn rewards!")
