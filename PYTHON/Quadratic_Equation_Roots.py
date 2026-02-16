# Quadratic Equation Roots

# Uma equação quadrática é representada como ax² + bx + c = 0.
# A fórmula geral para encontrar suas raízes (valores de x para os quais y = 0) é:
# x1,2 = -b +- raiz(b ** 2 - 4ac)
# exemplo
# Esta fórmula fornece duas raízes: x₁ e x₂. O valor dentro da raiz quadrada,
# b² - 4ac, é conhecido como discriminante (D). Com base no valor do discriminante, uma equação quadrática pode ter:
# duas raízes reais distintas (D > 0);
# uma raiz real (D = 0);
# nenhuma raiz real (D < 0).

# Seu código deve retornar um iterável contendo dois valores:
# as raízes x₁ e x₂, ordenadas em ordem decrescente.
# Se houver apenas uma raiz real, ambos os valores serão iguais.
# Se não houver raízes reais, o iterável deverá conter a string "Nenhuma raiz real".

from collections.abc import Iterable
from typing import Union


def quadratic_roots(a: int, b: int, c: int) -> Iterable[Union[int | float] | str]:
    discriminatory = (b ** 2) - (4 * a * c)

    if (discriminatory < 0):
        return ['No real roots']

    discriminatory_root = discriminatory ** 0.5
    x1 = (-b + discriminatory_root) / (2*a)
    x2 = (-b - discriminatory_root) / (2*a)

    return sorted([x1, x2], reverse=True)


print("Example:")
print(list(quadratic_roots(1, 2, 3)))

# These "asserts" are used for self-checking
assert list(quadratic_roots(1, -3, 2)) == [2, 1]
assert list(quadratic_roots(1, 0, -1)) == [1, -1]
assert list(quadratic_roots(1, 2, 1)) == [-1, -1]
assert list(quadratic_roots(1, 0, 1)) == ["No real roots"]
assert list(quadratic_roots(1, 4, 4)) == [-2, -2]
assert list(quadratic_roots(1, -5, 6)) == [3, 2]
assert list(quadratic_roots(1, -6, 9)) == [3, 3]
assert list(quadratic_roots(2, 2, 1)) == ["No real roots"]
assert list(quadratic_roots(2, -7, 6)) == [2, 1.5]
assert list(quadratic_roots(2, -3, 1)) == [1, 0.5]

print("The mission is done! Click 'Check Solution' to earn rewards!")
