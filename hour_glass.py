import math
import os
import random
import re
import sys
import numpy as np

# Complete the repeatedString function below.
def repeatedString(arr):
    s = []
    for i in range(len(arr)-2):
        for j in range(len(arr)-2):
            s.append(sum(arr,i,j))
    return max(s)
def sum(arr,i,j):
    s = arr[i,j] + arr[i,j+1] + arr[i,j+2] + arr[i+1,j+1] + arr[i+2,j] + arr[i+2,j+1] + arr[i+2,j+2]
    return s
    
    
     

if __name__ == '__main__':
    arr = np.array([(1,1,1,0,0,0),
                (0,1,0,0,0,0),
                (1,1,1,0,0,0),
                (0,0,2,4,4,0),
                (0,0,0,2,0,0),
                (0,0,1,2,4,0)])
    print(repeatedString(arr))
    