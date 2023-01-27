
def get_next_multiple(n):

    value = n

    while True:
        yield n
        n += value


generator = get_next_multiple(2)

for _ in range(5):
    print(next(generator))