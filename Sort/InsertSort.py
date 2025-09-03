def insert_sort(array):##用i遍历数组，默认i前面的都已经是顺序的数组，每次遍历将i融入前面已经排序的数组
    n = len(array)
    for i in range(1,n):
        temp = array[i]
        j=i-1
        if array[j]>temp:
            while array[j] >= temp and j>=0:
                array[j+1] = array[j]
                j-=1
            array[j+1]=temp
    return array
l=[6,2,7,5,10,22,11]
print(insert_sort(l))