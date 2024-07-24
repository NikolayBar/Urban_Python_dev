def get_password(in_num: int) -> str:
    res = ''
    for i in range(1, in_num):
        for j in range(i, in_num):
            if i == j:
                continue
            if in_num % (i + j) == 0:
                res += str(i) + str(j)
    return res


n = int(input())
result = get_password(n)
print(result)
