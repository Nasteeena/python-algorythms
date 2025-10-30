def find_index(list_of_num, num):
    for i in range(len(list_of_num)):
        if list_of_num[i] == num:
            return i
    return -1

# using index()

print([5, 3, 7, 3].index(8))
print("Привет".index("и"))