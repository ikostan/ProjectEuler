#!/usr/bin/python


import time


def find_maximum_total(triangle: list):
    start_time = time.time()
    new_triangle = triangle

    for n in range(0, len(new_triangle) - 1):
        if len(new_triangle[n]) < 2:
            new_triangle[n + 1][0] += new_triangle[n][0]
            new_triangle[n + 1][1] += new_triangle[n][0]
        else:
            for i in range(0, len(new_triangle[n]) + 1):
                #print('n: {0}, i: {1}, len: {2}'.format(n, i, len(new_triangle[n])))
                if i - 1 < 0:
                    new_triangle[n + 1][i] += new_triangle[n][i]
                elif i - 1 >= 0 and i < len(new_triangle[n]):
                    temp = max(new_triangle[n][i - 1], new_triangle[n][i])
                    new_triangle[n + 1][i] += temp
                else:
                    new_triangle[n + 1][i] += new_triangle[n][i - 1]
                print(new_triangle)

    result = max(new_triangle[-1])
    end_time = time.time() - start_time
    print_time_log(end_time, result)
    return result


# This function is used for logging processing time only
# Shows how long it took in order to get the answer
def print_time_log(end_time: time, result):
    if end_time < 60:
        print("The answer {0} returned in {1} seconds".format(
            result, end_time))
    else:
        minutes = int(end_time / 60)
        seconds = end_time - (minutes * 60)
        print("The answer {0} returned in {1} minutes and {2} seconds".format(
            result, minutes, seconds))

