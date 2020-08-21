"""
We define the distance between two array values as the number of indices between the two values.
Given a, find the minimum distance between any pair of equal elements in the array.
If no such value exists, print -1
For example, if a = = [3,2,1,2,3] , there are two matching pairs of values: 3 and 2.
so min distance is 0-4=4 and 3-1=2  return 2 
"""
def minimumDistance(a):
    dis=[]
    for i in range(len(a)):
        for j in range(len(a)):
            if a[i] == a[j] and i != j:
               distance = abs(i-j)
               dis.append(distance)            
    if len(dis) == 0:
        return -1
    else:
        return min(dis)
if __name__ == "__main__":
    a = [7,1,3,4,1,7]
    result = minimumDistance(a)
    print(result)
