def last_occurrence(list_of_nums, num):
    index = -1
    for i in range(len(list_of_nums)):
        if list_of_nums[i] == num:
            index = i
    return index
