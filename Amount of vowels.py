# alphabet in string

def count_vowels(value_str):
    count = 0
    alp_vowels = 'аеёиоуыэюя'

    for i in value_str:
        if i in alp_vowels:
            count += 1

    return count

# alphabet in tuple or in list

def count_vowels_2(value_str):
    count = 0
    alp_vowels = ('а', 'е', 'ё', 'и', 'о', 'у', 'ы','э', 'ю', 'я')
    # alp_vowels = ['а', 'е', 'ё', 'и', 'о', 'у', 'ы', 'э', 'ю', 'я'] same as above

    for i in value_str:
        if i in alp_vowels:
            count += 1

    return count