"""
title: quick sort
author: Parth Sakpal
date_created: 10/3/2023
"""


def quickSort(LIST, FIRST_INDEX, LAST_INDEX):

    """
    quick sort
    :param LIST: list(int)
    :param FIRST_INDEX:
    :param LAST_INDEX:
    :return:
    """

    if FIRST_INDEX < LAST_INDEX:
        PIVOT_VALUE = LIST[FIRST_INDEX]

        LEFT_INDEX = FIRST_INDEX + 1
        RIGHT_INDEX = LAST_INDEX

        DONE = False

        while not DONE:
            while LEFT_INDEX <= RIGHT_INDEX and LIST[LEFT_INDEX] <= PIVOT_VALUE:
                LEFT_INDEX += 1
            while RIGHT_INDEX >= LEFT_INDEX and LIST[RIGHT_INDEX] >= PIVOT_VALUE:
                RIGHT_INDEX -=1

            if RIGHT_INDEX < LEFT_INDEX:
                DONE = True

            else:
                TEMP = LIST[LEFT_INDEX]

                LIST[LEFT_INDEX] = LIST[RIGHT_INDEX]

                LIST[RIGHT_INDEX] = TEMP

        TEMP = LIST[FIRST_INDEX]
        LIST[FIRST_INDEX] = LIST[RIGHT_INDEX]
        LIST[RIGHT_INDEX] = TEMP


        quickSort(LIST, FIRST_INDEX, RIGHT_INDEX - 1)
        quickSort(LIST, RIGHT_INDEX + 1, LAST_INDEX)


if __name__ == "__main__":
    from myFunctions import *

    TIMES = []

    for i in range(30):
        NUMBERS = getRandomList(10000)
        START_TIME = getTime()
        quickSort(NUMBERS, 0, len(NUMBERS)-1)
        END_TIME = getTime()
        TIMES.append(END_TIME-START_TIME)
        print(i)

    print(getAverage(TIMES))

