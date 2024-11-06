import string


# Task 1
def not_range(start, end):
    if start < end:
        raise ValueError("start value cannot be greater then end")

    while start >= end:
        yield start
        start -= 1


# for i in not_range(10, 5):
#     print(i, end=" ")


# Task 2
def fibonacci_5():
    number_1 = 0
    number_2 = 1
    while True:
        number_1, number_2 = number_2, number_1 + number_2

        while number_2 % 5 != 0:
            number_1, number_2 = number_2, number_1+number_2
        yield number_2


# for i in fibonacci_5():
#     print(i)


# Task 3
def inf_factorial():
    n = 1
    factorial = 1

    while True:
        yield factorial
        n += 1
        factorial *= n


# for i in inf_factorial():
#     print(i)


# Task 4
def alphabet():
    list_alphabet = string.ascii_lowercase
    while True:
        for letter in list_alphabet:
            yield letter


# for i in alphabet():
#    print(i)


# Task 5
def unique_word(line):
    line = line.split(" ")
    words = []
    for word in line:
        if word not in words:
            words.append(word)
            yield word


# for i in unique_word("apple orange apple banana orange"):
#     print(i)


# Task 6
def len_words_greater_then(line, min_size):
    line = bubble_sort(line.split(" "))
    line = list(filter(lambda x: len(x) > min_size, line))

    for i in range(0, len(line), 1):
        yield line[i]


def bubble_sort(array: list) -> list:
    copy_arr = array.copy()
    length_array = len(copy_arr)

    for i in range(0, length_array-1, 1):
        for j in range(0, length_array-i-1, 1):
            if copy_arr[j] < copy_arr[j+1]:
                copy_arr[j], copy_arr[j+1] = copy_arr[j+1], copy_arr[j]

    return copy_arr


# for k in len_words_greater_then("Python is an amazing programming language", 4):
#     print(k)


# Task 7
def rotation_string(line, n):
    if len(line) < n:
        raise ValueError("length line less then second argument")

    def bulkhead_letters(lst: str, max_count: int):
        if len(lst) >= max_count:
            yield lst
            return

        for j in line:
            if j not in lst:
                yield from bulkhead_letters(lst+j, max_count)

    for k in range(1, n+1, 1):
        yield from bulkhead_letters("", k)


for i in rotation_string("Python", 2):
    print(i, end=" ")


# Task 8
def vowel_sounds(line):
    sounds = ["a", "e", "i", "o", "u", "y"]
    results = []
    for i in line:
        if i in sounds and i not in results:
            results.append(i)
            yield i


# for i in vowel_sounds("programming is enjoyable"):
#     print(i)

