def factorail(n):
    if n == 1:
        return 1
    return n * factorail(n - 1)

print(factorail(4))
