A = [0, 35, 12, 99, 18, 56, 73, 41, 64, 27, 5, 88, 3, 50, 67, 14, 92, 38, 21, 60]

def shellSort(array):
    d = len(array)//2
    n=len(array)
    while d >= 1:
        i=1
        while i<=d:##i表示第几个组
            m=d
            while m+i<n:## m表示当前偏移量, m+i表示组内具体位置
                ##执行组内插入排序
                if array[m+i] < array[m+i-d]:##如果下一个元素小于前面的元素
                    array[0] = array[m+i]
                    temp=m+i-d ##temp从哪个元素开始对比
                    while temp>0:
                        if array[temp]>array[0]:
                            array[temp+d]=array[temp]
                            temp-=d
                        else:
                            break
                    array[temp+d]=array[0]
                array[0]=0
                m += d
            i+=1
        d//=2
    return array

print(shellSort(A))