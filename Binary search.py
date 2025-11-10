def binary_search(list_of_nums, num):
    min = 0
    max = len(list_of_nums) - 1
    while min <= max:
        medium = (min + max) // 2
        if list_of_nums[medium] == num:
            return medium
        elif list_of_nums[medium] < num:
            min = medium + 1
        elif list_of_nums[medium] > num:
            max = medium - 1
    return -1