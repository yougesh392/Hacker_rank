"""
Print an integer denoting the minimum number, 
of bribes needed to get the queue into its final state.
Print Too chaotic if the state is invalid, i.e. 
it requires a person to have bribed more than  people.
"""

def chaos_checker(n,l):
    moves = 0
    for pos, val in enumerate(q):
        if (val-1) - pos > 2:
            print("Too chaotic")
            return
        for j in range(max(0,val-2), pos):
            if q[j] > val:
                moves+=1
    return moves
    
if __name__ == "__main__":
    n = 5
    q = [2, 5, 1, 3 ,4]
    print(chaos_checker(n,q))
