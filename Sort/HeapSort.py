##大根堆，Heapsort只输出一个副本，不改变大根堆，delete在大根堆上进行，build把原本乱序数组构造成一个大根堆
def HeapSort(array):
    temp = array.copy()
    n=len(temp)
    for i in range(n-1,0,-1):##获得有序序列
        temp[0],temp[i]=temp[i],temp[0]
        shift_down(temp,0,i-1)
    return temp

def build_heap(array,n):
    for i in range(n // 2 - 1, -1, -1):  ##构造大根堆
        shift_down(array, i, n - 1)
    return array

def shift_down(array,i,n):
    x = 2 * i + 1  ##x是左孩子
    while x<=n:
        if x+1<=n and array[x+1]>array[x]:
            x=x+1
        if array[x]<array[i]:
            break
        array[x],array[i]=array[i],array[x]
        i=x
        x=2*x+1
    return array

def shift_up(array,i):
    while i>0:
        p = (i-1)//2
        if array[p]<array[i]:
            array[i],array[p]=array[p],array[i]
            i = p
        else:
            break
    return array

def delete_node(array,x):
    for i in range(len(array)):
        if array[i]==x:
            array[i] = array[len(array)-1]
            array.pop(len(array)-1)
            if i >= len(array):
                return array
            if i>0 and array[i]>array[(i-1)//2]:
                shift_up(array,i)
            else:
                shift_down(array,i,len(array)-1)
            return array
    return -1

text = [9,8,7,6,5,23,4,3,2,1]
print(build_heap(text,len(text)))
print(HeapSort(text))
print(delete_node(text, 23))
print(HeapSort(text))
