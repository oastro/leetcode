# Convert Date

# Essa função deve pegar uma string de data no formato dd/mm/yyyy
# e convertê-la para o formato yyy-mm-dd.
#  Se a entrada não estiver no formato correto,
# a função deve devolver a mensagem de erro "Erro: Data inválida.".

def convert_date(date: str) -> str:
    error = "Error: Invalid date."

    if (len(date) != 10):
        return error

    day, month, year = map(int, date.split('/'))

    if (month > 12):
        return error

    if (month in [4, 6, 9, 11] and day == 31):
        return error

    def is_LeapYear(year):
        return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

    if (month == 2 and day == 29 and not is_LeapYear(year)):
        return error

    result = f"{year}-{month:02d}-{day:02d}"

    return result


print("Example:")
print(convert_date("01/01/2023"))

# These "asserts" are used for self-checking
assert convert_date("25/12/2021") == "2021-12-25"
assert convert_date("01/01/2000") == "2000-01-01"
assert convert_date("15/06/1995") == "1995-06-15"
assert convert_date("29/02/2020") == "2020-02-29"
assert convert_date("10/10/2010") == "2010-10-10"
assert convert_date("31/05/1985") == "1985-05-31"
assert convert_date("07/08/1960") == "1960-08-07"
assert convert_date("02/09/1999") == "1999-09-02"
assert convert_date("30/04/1975") == "1975-04-30"
assert convert_date("29/02/2019") == "Error: Invalid date."
assert convert_date("30/04/1975/1") == "Error: Invalid date."

print("The mission is done! Click 'Check Solution' to earn rewards!")
