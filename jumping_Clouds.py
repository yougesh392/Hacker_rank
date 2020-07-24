import math
import os
import random
import re
import sys

# Complete the jumpingOnClouds function below.
def jumpingOnClouds(c,n):
    current = 0;
    jump = 0;
    
    while current < n:
        if((current + 2) < n and c[current + 2] == 0 ):
            jump = jump + 1
            current = current + 2
        elif (c[current + 1] == 0):
            jump = jump + 1
            current = current + 1
    return jump
    
    

if __name__ == '__main__':
    n = 6
    c = [0,0,0,0,1,0]
    result = jumpingOnClouds(c,n)

    