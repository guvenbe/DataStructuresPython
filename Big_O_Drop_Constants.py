# O(n+n) = O(2n)
# We drop the 2
# so it O(n)

def print_items(n):
    for i in range(n):
        print(i)

    for j in range(n):
        print(j)

print_items(10)


