
def double_values(fun):
    
    def inner(a, b) -> float:

        return fun(a * 2, b * 2)
    
    return inner


@double_values
def add(a, b) -> float:
    return a + b


print(add(2, 3))