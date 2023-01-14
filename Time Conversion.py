#!/bin/python3

import math
import os
import random
import re
import sys

#
# Complete the 'timeConversion' function below.
#
# The function is expected to return a STRING.
# The function accepts STRING s as parameter.
#

def timeConversion(s):
    # Write your code here
    if(s[8:10] == 'PM'):
        if(s[0:2] == '12'):
            result = s[:8]
        else:
           result = str(int(s[0:2])+12)+s[2:8] 
    else:
        if(s[0:2] == '12'):
            result = '00'+s[2:8]
        else:
            result = s[:8]
    return result
  

  


if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    s = input()

    result = timeConversion(s)

    fptr.write(result + '\n')

    fptr.close()
