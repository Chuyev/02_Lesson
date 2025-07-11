def is_year_leap(year):

    if year % 400 == 0:
        return True
    if year % 100 == 0:
        return False
    if year % 4 == 0:
        return True
    return False

# Примеры использования:
print(is_year_leap(2020))  # True (делится на 4)
print(is_year_leap(1900))  # False (делится на 100)
print(is_year_leap(2000))  # True (делится на 400)
print(is_year_leap(2021))  # False