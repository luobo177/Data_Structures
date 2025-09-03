#快排,随机选取一个数，避免顺序和倒序的最坏情况
import random
text = [9,8,7,6,51,23,4,3,2,1]

def quickSort(array,low,high):##负责划分子数组
    if low < high:
        pivot = partition(array,low,high)
        quickSort(array,pivot+1,high)##右边
        quickSort(array,low,pivot-1)##左边
    return array


def partition(array,low,high):##负责子数组的排序
    r = random.randint(low,high)
    array[low],array[r] = array[r],array[low]
    pivot = array[low]
    while low < high:
        while low < high and array[high] >= pivot:
            high -= 1
        array[low] = array[high]
        while low < high and array[low] <= pivot:
            low += 1
        array[high] = array[low]
    array[low] = pivot
    return low

print(quickSort(text,0,len(text)-1))