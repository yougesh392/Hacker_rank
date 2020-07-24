import math
import os
import random
import re
import sys

# Complete the countingValleys function below.
def countingValleys(n, s):
    h = 0
    p_h = 0
    ct = 0
    for i in range(len(s)):
        if(s[i]=='U'):
            h = h+1
        elif(s[i]=='D'):
            h = h-1
        if (h == 0 and p_h < 0):
            ct = ct + 1
        p_h = h
    return(ct)


if __name__ == '__main__':
    
    n = 8
    s = "UDDDUDUU"
    result = countingValleys(n, s)
    print(result)
    