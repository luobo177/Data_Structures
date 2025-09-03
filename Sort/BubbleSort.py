##基于数组实现冒泡排序，从头开始遍历，大的在后边
text = [9,8,7,6,5,23,4,3,2,1]
def bubbleSort(array):
    n=len(array)
    for i in range(n-1): ##i为已经排序的个数
        is_swapped = False
        for j in range(0,n-i-1): ##j为从0开始往后遍历的指针,遍历到n-i个为止，因为后面的已经有序
            if array[j]>array[j+1]:
                array[j],array[j+1]=array[j+1],array[j]
                is_swapped = True
        if not is_swapped: break
    return array

print(bubbleSort(text))