"""
title: Bubble Sort
author: Parth Sakpal
date-created: 9/14/2023
"""





def bubbleSort(LIST):
    '''
    compares two adjacent values and places the highest one at the end
    :param LIST: list(int)
    :return: none
    '''


    # range(start, stop, step)
    for i in range(len(LIST)-1, 0, -1): # traverse backward until the 2nd position
        for j in range(i): # traverse forward until the sorted value index
            if LIST[j] > LIST[j+1]:
                TEMP = LIST[j]
                LIST[j] = LIST[j+1]
                LIST[j+1] = TEMP



if __name__ == "__main__":
    from myFunctions import *

    TIMES = []

    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        bubbleSort(NUMBERS)
        END_TIME = getTime()
        TIMES.append(END_TIME - START_TIME)
        print(i)
    print(getAverage(TIMES))

