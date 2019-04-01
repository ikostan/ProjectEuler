#!/usr/bin/python


import time


def number_to_words_counter(numbers: list):

    start_time = time.time()

    nums_0_19 = ['', 'One', 'Two', 'Three', 'Four', 'Five', 'Six',
                 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen',
                 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen']

    nums_20_90 = ['Twenty', 'Thirty', 'Forty', 'Fifty',
                  'Sixty', 'Seventy', 'Eighty', 'Ninety']

    nums_dict = {100: 'hundred', 1000: 'thousand',
                 1000000: 'million', 1000000000: 'billion'}

    result = ''

    for n in numbers:
        temp = ''
        try:
            if n < 20:
                temp = nums_0_19[n]
            elif n < 100:
                temp = nums_20_90[(n // 10) - 2] + nums_0_19[n % 10]
            elif n < 1000:
                temp = nums_0_19[n // 100] + nums_dict[100]

                if n % 100 != 0:
                    if n % 100 < 20:
                        temp += 'and' + nums_0_19[n % 100]
                    elif n % 100 < 100:
                        temp += 'and' + nums_20_90[((n % 100) // 10) - 2]
                        if (n % 100) % 10:
                            temp += nums_0_19[(n % 100) % 10]
            elif n < 10000:
                temp = nums_0_19[n // 1000] + nums_dict[1000]

            #print(str(n) + " : " + temp)
            result += temp
        except IndexError:
            print("Error on number: " + str(n))

    result = len(result)
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

