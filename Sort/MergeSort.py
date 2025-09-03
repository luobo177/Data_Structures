##合并排序
def merge_sort(array,low,high):
    if low >= high:
        return array
    mid = (low+high)//2
    print(array[low:high+1])
    merge_sort(array,low,mid)
    merge_sort(array,mid+1,high)
    merge(array,low,mid,high)
    return array



def merge(array,low,mid,high):
    B = [0]*len(array)
    for i in range(low,high+1,1):
        B[i]=array[i]
    i,j=low,mid+1
    n=low
    while i<=mid and j<=high:
        if B[i]<=B[j]:
            array[n] = B[i]
            i+=1
        else:
            array[n] = B[j]
            j+=1
        n+=1
    while i<=mid:
        array[n] = B[i]
        i+=1
        n+=1
    while j<=high:
        array[n] = B[j]
        j+=1
        n+=1
    return array

text = [2,5,8,11,46,3,6,10,55]
print(merge_sort(text,0,len(text)-1))