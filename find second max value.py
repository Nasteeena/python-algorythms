def new_function(list_of_numbers):
    max = list_of_numbers[0]
    max_after_max = list_of_numbers[0]
    for i in list_of_numbers:
        if i > max:
            max_after_max = max
            max = i
        if i > max_after_max and i != max:
            max_after_max = i
    print(max_after_max)

new_function([1,3,9,8,2,1])
