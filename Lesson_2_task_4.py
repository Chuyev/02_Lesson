n = int(input("Введите число: "))


def fizz_buzz(n):
    """
    Выводит числа от 1 до n, заменяя:
    - числа, кратные 3, на 'Fizz'
    - числа, кратные 5, на 'Buzz'
    - числа, кратные 15, на 'FizzBuzz'
    """
    for i in range(1, n+1):
        if i % 15 == 0:
            print("FizzBuzz")
        elif i % 3 == 0:
            print("Fizz")
        elif i % 5 == 0:
            print("Buzz")
        else:
            print(i)


fizz_buzz(n)
