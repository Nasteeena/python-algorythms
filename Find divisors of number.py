def find_divisors(num):
    index = 1
    while index <= num:
        if num % index == 0:
            print(index)
        index += 1

find_divisors(10)