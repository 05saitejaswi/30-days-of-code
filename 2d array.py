
import math
import os
import random
import re
import sys



if __name__ == '__main__':
    arr = []

    for _ in range(6):
        arr.append(list(map(int, input().rstrip().split())))
sums = [0]*16

for i in range(16):
    sums[i] += sum(arr[i//4][i%4:i%4+3])+ sum(arr[i//4+2][i%4:i%4+3])+ arr[i//4+1][i%4 + 1]
print(max(sums))
