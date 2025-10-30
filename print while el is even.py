def count_el(lIst):
    index = 0
    while lIst[index] % 2 == 0:
        print(lIst[index])
        index += 1

count_el([10,8, 12, 3, 4])