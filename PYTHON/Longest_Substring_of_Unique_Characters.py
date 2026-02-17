# Longest Substring of Unique Characters

# Dada uma sequência, encontre o comprimento da substring mais longa sem repetir caracteres.

def longest_substr(s: str) -> int:
    max_lenght = 0

    for index in range(len(s)):
        char = set()

        for indexJ in range(index, len(s)):
            if s[indexJ] in char:
                break

            char.add(s[indexJ])
            max_lenght = max(max_lenght, indexJ - index + 1)

    return max_lenght


print("Example:")
print(longest_substr("abcabcbb"))

# These "asserts" are used for self-checking
assert longest_substr("abcabcbb") == 3
assert longest_substr("bbbbb") == 1
assert longest_substr("pwwkew") == 3
assert longest_substr("abcdef") == 6
assert longest_substr("") == 0
assert longest_substr("au") == 2
assert longest_substr("dvdf") == 3

print("The mission is done! Click 'Check Solution' to earn rewards!")
