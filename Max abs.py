def max_abs(num_list):
    max = num_list[0]

    for num_value in num_list:
        num_index = num_value if num_value >= 0 else -num_value
        num_abs_initial = max if max >= 0 else -max

        if num_index > num_abs_initial:
            max = num_value

    return max

