def solution(A):
    N = len(A)
    B = [0] * N

    for i in range(N):
        if B.count(A[i]) == 0:
            B[i] = A[i]
        else:
            #B[i] = A[i]-1
            B[i] = findBigNo(B, A[i]-1)
    return B

def findBigNo(B, num):

    while num >=0:

        if B.count(num) == 0:
            return num
        else:
            num = num - 1
            findBigNo(B, num)
    return num
