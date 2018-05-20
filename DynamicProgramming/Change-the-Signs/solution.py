import sys
sys.setrecursionlimit(1000000)

A = []
memo = {}
parent_pointer = {}

def recursive_Signs(index):
    global memo, parent_pointer
    if index >= len(A):
        return 0

    if index in memo:
        return memo[index]

    pos = A[index] + recursive_Signs(index+1)
    neg = float("inf")
    length = len(A)
    left_check = (index == 0 or A[index-1] - A[index] > 0)
    right_check = (index == length - 1 or A[index+1] - A[index] > 0)
    swallow_check = (index >= length - 2 or A[index+2] + A[index] >= A[index+1])

    if right_check and left_check > 0:
        if swallow_check:
            neg = recursive_Signs(index+3) - A[index] + (A[index + 1] if index <= length - 2 else 0) \
             + (A[index + 2] if index <= length - 3 else 0)
        else:
            neg = recursive_Signs(index+2) - A[index] + (A[index + 1] if index <= length - 2 else 0)

    if neg < pos:
        parent_pointer[index] = -1

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

