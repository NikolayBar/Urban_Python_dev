# n = [x for x in range(3, 7)]

def get_password(in_num: int) -> str:
    res = ''
    for i in range(1, in_num):
        for j in range(2, in_num):
            if i == j:
                continue
            if (i + j) % in_num == 0:
                res += str(i) + str(j)
    return res


print(get_password(6))

# answ = {3: '12',
#         4: '13',
#         5: '1423',
#         6: '121524',
#         7: '162534',
#         8: '13172635',
#         9: '1218273645',
#         10: '141923283746',
#         11: '11029384756',
#         12: '12131511124210394857',
#         13: '112211310495867',
#         14: '1611325212343114105968',
#         15: '1214114232133124115106978',
#         16: '1317115262143531341251161079',
#         17: '11621531441351261171089',
#         18: '12151811724272163631545414513612711810',
#         19: '118217316415514613712811910',
#         20: '13141911923282183731746416515614713812911'}


# for k in range(3, 21):
#     if k in (4, 5):
#         continue
#     assert get_password(k) == answ[k], f'{k}: fn - {get_password(k)}, answ - {answ[k]}'


