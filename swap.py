import math
import os
import random
import re
import sys

# Complete the minimumSwaps function below.
def minimumSwaps(arr): 
    count = 0; 
    i = 0; 
    while (i < len(arr)): 
        
        if (arr[i] != i + 1): 
  
            while (arr[i] != i + 1): 
                
                temp = arr[arr[i] - 1]; 
                arr[arr[i] - 1] = arr[i]; 
                arr[i] = temp; 
                count += 1; 
                print(arr) 
        i += 1; 
    return count; 
    

if __name__ == '__main__':
    n = 4

    arr = [4,3,1,2]
    print(arr)
    res = minimumSwaps(arr)
    
    print(res)
