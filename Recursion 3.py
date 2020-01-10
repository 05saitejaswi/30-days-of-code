
import math
import os
import random
import re
import sys

# Complete the factorial function below.
def factorial(n):
     return math.factorial(n)
if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    result = factorial(n)

    fptr.write(str(result) + '\n')

    fptr.close()
