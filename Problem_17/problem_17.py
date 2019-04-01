#!/usr/bin/python


import time


def number_to_words(numbers: list):

    start_time = time.time()

    nums_0_19 = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
                 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
                 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    nums_20_90 = ['Twenty', 'Thirty', 'Forty', 'Fifty',
                  'Sixty', 'Seventy', 'Eighty', 'Ninety']

    nums_dict = {100: 'hundred', 1000: 'thousand',
                 1000000: 'million', 1000000000: 'billion'}

    result = ''

    for n in numbers:
        if n < 20:
            result += nums_0_19[n]

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
