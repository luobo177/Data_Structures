##计数排序，这版如果有负数，则全体右移，使全部为正数，然后排序完了再左移回去，move为是否移动


def countSort(A,n,k):##A为输入数组，B为输出数组，n为数组长度，k为数组里的最大值
    ##右移逻辑
    move = 0
    m=findMinCount(A)
    if m<0:
        k -= m
        move = 1
        for i in range(n):
            A[i]+=-m

    ##排序逻辑
    B=[0]*(k+1)
    temp=A.copy()
    for i in range(n):
        B[A[i]]+=1
    for i in range(1,k+1):
        B[i]+=B[i-1]
    i = n-1
    while i >=0:
        A[B[temp[i]]-1]=temp[i]
        B[temp[i]]-=1
        i-=1

    ##左移逻辑
    if move == 1:
        for i in range(n):
            A[i] += m
    return A

##找最大值
def findBiggestCount(array):
    n = len(array)
    m = array[0]
    for i in range(n):
        if array[i] > m:
            m = array[i]
    return m

##找最小值
def findMinCount(array):
    n = len(array)
    m = array[0]
    for i in range(n):
        if array[i]<m:
            m = array[i]
    return m


text = [9,8,7,6,2,3,11,45,-21,-2,33,22,11,4,3,2,1,1,1]
print(countSort(text,len(text),findBiggestCount(text)))

