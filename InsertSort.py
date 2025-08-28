def insert_sort(array):
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