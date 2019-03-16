def get_multiplies_of_3_and_5(num):
    result = 0
    i = 3

    while i < num:
        if i % 3 == 0 or i % 5 == 0:
            result += i
        i += 1

    return result

