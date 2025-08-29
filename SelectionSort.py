text = [9,8,7,6,51,23,4,3,2,1]
##简单选择算法：选一个i以后的最小值放到已排序的数组队列的最后面
def selection_sort(array):
    n=len(array)
    for i in range(n-1):
        locate = i##locate表示每次遍历找到的最小值的下标
        for j in range(i+1,n):
            if array[j]<array[locate]:
                locate = j
        array[i],array[locate] = array[locate],array[i]
    return array

print(selection_sort(text))
