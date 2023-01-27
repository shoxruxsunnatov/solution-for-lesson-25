
def check_arg(fun):

    def inner(l: list) -> int:

        if not isinstance(l, list):
            return 'Only <list> type is allowed!'
        
        return fun(l)
    
    return inner


@check_arg
def sum_index(l: list) -> int:
    
    if l:
        return len(l) - 1
    else:
        return 0

print(sum_index((2,3)))