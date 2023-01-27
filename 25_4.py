
def only_even_numbers(fun):

    def inner(*args) -> float:

        for arg in args:
            if arg % 2 != 0:
                return 'Only even numbers allowed!'

        return fun(*args)
    
    return inner


@only_even_numbers
def multiply(a, b, c, d) -> float:
    return a * b * c * d


@only_even_numbers
def add(a, b) -> float:
    return a + b


print(add(4, 3))
print(multiply(6, 2, 2, 4))