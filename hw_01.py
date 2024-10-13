# Task 1
def count_calls(function):
    counter = 0

    def wrapper(*args, **kwargs):
        nonlocal counter
        counter += 1
        print(f"Number of function calls '{function.__name__}': {counter}'")

        function(*args, **kwargs)

    return wrapper


@count_calls
def print_name(name):
    print(f"Hello, {name}!")


# print_name("Name 1")
# print_name("Name 2")
# print_name("Name 3")

# END Task 1

# -----

# Task 2
def type_check(*expected_types: type):
    def decorator(function):
        def wrapper(*args):
            if len(expected_types) != len(args):
                raise ValueError("Incorrect count expected types")

            for i in range(0, len(expected_types), 1):
                if not isinstance(args[i], expected_types[i]):
                    raise TypeError(f"Invalid argument {i}. Expected {expected_types[i]}, received {type(args[i])}")

            return function(*args)
        return wrapper

    return decorator


@type_check(int, int)
def summa(a, b):
    return a + b


# print(summa(1, 2))
# print(summa(1, 1.2))
# print(summa("2", 1))

# END Task 2

# -----

# Task 3
def validate_range(min_value: int or float, max_value: int or float):
    def decorator(function):
        def wrapper(*args, **kwargs):
            for i in range(0, len(args), 1):
                if args[i] > max_value or args[i] < min_value:
                    raise ValueError(f"Argument {i} has a value of {args[i]}, which goes beyond [{min_value}, {max_value}]")

            for i in kwargs.keys():
                if kwargs[i] > max_value or kwargs[i] < min_value:
                    raise ValueError(f"Argument {i} has a value of {kwargs[i]}, goes beyond [{min_value}, {max_value}]")

            return function(*args, **kwargs)

        return wrapper

    return decorator


@validate_range(min_value=0, max_value=100)
def set_percentage(value):
    print(f"Set value: {value}%")


# print(set_percentage(12))
# print(set_percentage(100))
# print(set_percentage(-10))
# print(set_percentage(value=23))
# print(set_percentage(value=120))

# END Task 3

# -----

# Task 4
def trace(function):
    def wrapper(*args, **kwargs):
        tab = '    ' * wrapper.call_depth
        print(f"{tab} --> Enter in function {function.__name__} with arguments {args}")
        wrapper.call_depth += 1

        result = function(*args, **kwargs)

        wrapper.call_depth -= 1
        print(f"{tab} <-- Exit from function {function.__name__} with result {result}")
        return result

    wrapper.call_depth = 0
    return wrapper


@trace
def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


#factorial(3)

# END Task 4

# -----

# Task 5
def uppercase_result(function):
    def wrapper(*args, **kwargs):
        result = function(*args, **kwargs)
        if isinstance(result, str):
            result = result.upper()

        return result
    return wrapper


@uppercase_result
def get_greeting(name):
    return f"Hello, {name}"


@uppercase_result
def add_numbers(a, b):
    return a+b


# print(get_greeting("Name 1"))
# print(add_numbers(2, 3))

# END Task 5

# -----

# Task 6
def call_limit(max_calls):
    counter = 0

    def decorator(function):
        def wrapper(*args, **kwargs):
            nonlocal counter
            counter += 1
            if counter > max_calls:
                raise RuntimeError("The maximum number of function calls has been exceeded")

            return function(*args, **kwargs)
        return wrapper
    return decorator


@call_limit(max_calls=3)
def print_message(msg):
    print(msg)


# print_message("some massage 1")
# print_message("some massage 2")
# print_message("some massage 3")
# print_message("some massage 4")

# END Task 6
