my_list = [42, 69, 0, 322, 13, 0, 99, -5, 9, 8, 7, -6, 5]

indx = -1

while indx < len(my_list)-1:
    indx += 1
    if my_list[indx] > 0:
        print(my_list[indx])
    elif my_list[indx] == 0:
        continue
    else:
        break
