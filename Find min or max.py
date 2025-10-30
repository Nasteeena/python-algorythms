def find_min(list_of_numbers):
    min = list_of_numbers[0]

    for i in list_of_numbers:
        if i < min:
            min = i

    return  min

