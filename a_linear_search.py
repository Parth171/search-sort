'''
title: Simply Linear Search
author: Parth Sakpal
date-created: 9/8/2022
'''

# 0.36272
# 0.3294


import time, random, statistics

# make a large order data set
NUMBERS = []
for i in range(20000000):
    if random.randrange(2) == 1:
        NUMBERS.append(i)


TIMES = []

for i in range(30):
    NUM = NUMBERS[random.randrange(len(NUMBERS))]

    # Linear Search

    START_TIME = time.perf_counter()
    for j in range(len(NUMBERS)):
        if NUMBERS[j] == NUM:
            print(f"{NUM} is found at index {j}")
            break

    END_TIME = time.perf_counter()
    TIMES.append(END_TIME - START_TIME)

print(statistics.mean(TIMES))