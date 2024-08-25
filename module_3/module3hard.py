def calculate_structure_sum(n):
    s = 0
    for el in n:
        if isinstance(el, dict):
            el = calculate_structure_sum(el.items())
        if isinstance(el, (list, tuple, set)):
            el = calculate_structure_sum(el)
        if isinstance(el, str):
            el = len(el)
        s += el
    return s


data_structure = [
    [1, 2, 3],
    {'a': 4, 'b': 5},
    (6, {'cube': 7, 'drum': 8}),
    "Hello",
    ((), [{(2, 'Urban', ('Urban2', 35))}])
]

result = calculate_structure_sum(data_structure)
print(result)
