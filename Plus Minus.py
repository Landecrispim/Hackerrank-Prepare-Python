#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'plusMinus' function below.
#
# The function accepts INTEGER_ARRAY arr as parameter.
#

def plusMinus(arr):
    # Write your code here
    print("%.6f" % (len([i for i in arr if(i>0)])/len(arr)))
    print("%.6f" % (len([i for i in arr if(i<0)])/len(arr)))
    print("%.6f" % (len([i for i in arr if(i==0)])/len(arr)))
    



if __name__ == '__main__':
    n = int(input().strip())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)