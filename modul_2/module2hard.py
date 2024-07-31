def get_password(in_num: int) -> str:
    res = ''
    for i in range(1, in_num // 2 + 1):
        for j in range(i + 1, in_num):
            if in_num % (i + j) == 0:
                res += str(i) + str(j)
    return res


# n = int(input())
# result = get_password(n)
# print(result)
