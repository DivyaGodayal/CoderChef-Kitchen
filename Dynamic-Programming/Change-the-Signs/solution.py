import sys
sys.setrecursionlimit(1000000)

A = []
memo = {}
parent_pointer = {}

# One dimensional dynamic programming state representation
def recursive_Signs(index):
    # the memoization cache and the parent_pointer dictionary to do the final backtracking
    global memo, parent_pointer

    # If we've reached the end of the array, no element left to process so return 0
    if index >= len(A):
        return 0

    # The state of the recursion is represented by 'index'. If we've processed an index before, we just return the cached result    
    if index in memo:
        return memo[index]

    # One recursion is where we don't negate the number at index 'i' and simply go to index 'i+1'
    pos = A[index] + recursive_Signs(index+1)
    
    neg = float("inf")
    length = len(A)

    # Check to see left side would be secure after negating the number at 'index'
    left_check = (index == 0 or A[index-1] - A[index] > 0)

    # Check to see right side would be secure after negating the number at 'index'
    right_check = (index == length - 1 or A[index+1] - A[index] > 0)

    # The SWALLOW check to maintain the correctness of the solution
    swallow_check = (index >= length - 2 or A[index+2] + A[index] >= A[index+1])

    # If right and left checks are satisfied, that means we can surely negate the number at 'index', question is where do we go next
    if right_check and left_check:
        # If SWALLOW check is satisfied, we go to 'index+3'. NOTE: we take care of the edge cases like the 'index' being the last number
        if swallow_check:
            neg = recursive_Signs(index+3) - A[index] + (A[index + 1] if index <= length - 2 else 0) \
             + (A[index + 2] if index <= length - 3 else 0)     
        else:
            neg = recursive_Signs(index+2) - A[index] + (A[index + 1] if index <= length - 2 else 0)

    # See what option gave us the minimum cost.        
    if neg < pos:
        # We only store those numbers in the parent_pointer dictionary which were negated. MEMORY saving!
        parent_pointer[index] = -1

    # Cache the result for this state.    
    memo[index] = min(pos, neg)
    return memo[index]


if __name__ == "__main__":
    T = int(input())
    for i in range(T):
        A = []
        memo = {}
        parent_pointer = {}
        min_sum = float("inf")
        A = []
        N = int(input())
        A = list(map(int, input().split()))
        if len(A) == 0 or len(A) == 1:
            print(A)
        else:
            recursive_Signs(0)
            i = 0
            while i < len(A):
                if i in parent_pointer:
                    swallow_check = (i >= len(A) - 2 or A[i+2] + A[i] >= A[i+1])
                    A[i] = -A[i]
                    if swallow_check:
                        i = i + 3
                    else:
                        i = i + 2
                else:
                    i = i + 1
            print(" ".join(list(map(str,A))))
