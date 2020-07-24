import math
import os
import random
import re
import sys

# Complete the rotLeft function below.
def leftrotation(a,d):
    return(a[d:] + a[:d])

if __name__ == '__main__':
    
    a = [1,2,3,4,5]
    d = 4
    result = leftrotation(a, d)
    print(result)