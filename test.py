def r_sum(n, s=None):
    s = 0 if s is None else s
    for el in n:
        if isinstance(el, list):
            r_sum(el, s)
        else:
            s += el
    return s

a = [1, 2, 3, [4, 5, 6]]

b = r_sum(a)
print(b)
