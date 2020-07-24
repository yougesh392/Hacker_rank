import math
import os
import random
import re
import sys

# Complete the repeatedString function below.
def repeatedString(s, n):
    repeats = 0
    remainders = 0
    number=s.count('a')
    if number==1 and len(s)==1:
        print(n)
    else:
        repeats=n//len(s) 
        remainders=n%len(s)
    return number * repeats+ s[:remainders].count('a') 

if __name__ == '__main__':
    s = 'a'
    n = 1000000000000
    repeatedString(s, n)
