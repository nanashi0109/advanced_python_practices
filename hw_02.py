from functools import reduce
from random import randint


# Task 1
array_1 = ["1", "20", "300"]

print("---Task 1---\n", array_1)
array_1 = list(map(lambda x: int(x), array_1))
print(array_1)


# Task 2
array_2 = [i for i in range(1, 10, 1)]

print("---Task 2---\n", array_2)
array_2 = list(filter(lambda x: x % 2 == 0, array_2))
print(array_2)


# Task 3
array_3 = [i for i in range(1, 10, 1)]

print("---Task 3---\n", array_3)
array_3 = list(map(lambda x: x**2, array_3))
print(array_3)


# Task 4
array_4 = ["cat", "elephant", "dog", "tiger"]
print("---Task 4---\n", array_4)
array_4 = list(filter(lambda x: len(x) > 3, array_4))
print(array_4)


# Task 5
array_5 = [1, 2, 3, 4, 5]
print("---Task 5---\n", array_5)
some_number = reduce(lambda x, y: x * y, array_5)
print(some_number)


# Task 6
array_6 = ["Hello", "World", "Python"]
print("---Task 6---\n", array_6)
array_6 = list(map(lambda x: len(x), array_6))
print(array_6)


# Task 7
array_7 = ["apple", "banana", "pear", "strawberry"]
print("---Task 7---\n", array_7)
number_7 = len(reduce(lambda x, y: x if len(x) > len(y) else y, array_7))
print(number_7)


# Task 8
array_8 = ["Hello", "World"]
print("---Task 8---\n", array_8)
array_8 = list(map(lambda x: x.upper(), array_8))
print(array_8)


# Task 9
array_9 = ["1", "2", "3", "4"]
print("---Task 9---\n", array_9)
array_9 = list(filter(lambda x: x % 2 == 0, map(lambda x: int(x) ** 2, array_9)))
print(array_9)


# Task 10
array_10 = [randint(-5, 5) for i in range(0, 10)]
print("---Task 10---\n", array_10)
array_10 = reduce(lambda x, y: x*y, filter(lambda x: x > 0, array_10))
print(array_10)


# Task 11
vowel_letters = ["a", "e", "i", "o", "u", "y"]
array_11 = ["apple", "banana", "orange", "grape"]
print("---Task 11---\n", array_11)
array_11 = list(map(lambda x: len(x), filter(lambda x: x[0].lower() in vowel_letters, array_11)))
print(array_11)


# Task 12
array_12 = ["racecar", "hello", "level", "world"]
print("---Task 12---\n", array_12)
array_12 = list(filter(lambda x: x == x[::-1], map(lambda x: x[::-1], array_12)))
# OR (result will not change)
# array_12 = list(filter(lambda x: x == x[::-1], array_12))
print(array_12)


# Task 13
def factorial(number):
    if number == 0:
        return 1
    else:
        return number * factorial(number - 1)


array_13 = [i for i in range(2, 7, 1)]
print("---Task 13---\n", array_13)
array_13 = reduce(lambda x, y: x*y, map(factorial, filter(lambda x: x % 2 == 0, array_13)))
print(array_13)


# Task 14
array_14 = ["hello", "world", "Python", "is", "great"]
print("---Task 14---\n", array_14)
array_14 = reduce(lambda x, y: f"{x} {y}", map(lambda x: x.upper(), filter(lambda x: len(x) % 2 == 0, array_14)))
print(array_14)


# -----------


# Task 1.1
def infinity_number_5():
    number = 5
    while True:
        yield number
        number += 5


# for i in infinity_number_5():
#     print(i)


# Task 1.2
def squares_all_int():
    number = 1
    while True:
        yield number ** 2
        number += 1


# for i in squares_all_int():
#     print(i)


# Task 1.3
def range_without_multiplicity_3(end):
    number = 1
    while number < end:
        yield number
        number += 1
        if number % 3 == 0:
            number += 1


# for i in range_without_multiplicity_3(10):
#     print(i)


# Task 1.4
def substrings_of_string(string, length):
    number = 0
    while number+2 < len(string):
        yield string[number: number+length]
        number += 1


# for i in substrings_of_string("abcdefgi", 3):
#     print(i)


# Task 1.5
def range_2(start, end):
    number = start
    while number <= end:
        yield number
        number += 2


# for i in range_2(1, 10):
#     print(i)


# Task 1.6
def infinity_random_number():
    while True:
        yield randint(0, 100)


# for i in infinity_random_number():
#     print(i)


# Task 1.7
def fibonacci_numbers():
    last = 0
    current = 1

    yield last
    yield current

    while True:
        yield last + current
        buff = last
        last = current
        current += buff


# for i in fibonacci_numbers():
#     print(i)

