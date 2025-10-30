def count_increase(num_list):
    count = 0
    for i in range(len(num_list) - 1):
        if num_list[i + 1] > num_list[i]:
            count += 1

    return count

print(count_increase([1, 3, 2, 4]))