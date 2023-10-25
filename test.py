print(ord("h"))
print(chr(104))

a, b = 'an', 'am'
print(a < b)

s = "string"
print(s[:])


def partial(lst, query):
    return [s for s in lst if query in s]


# Example 1:
print(partial(['hello', 'world', 'python', 'pyth'], 'py'))