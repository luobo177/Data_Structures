##匹配算法的kmp算法


def simple_match(main,match_list):
    total = len(main)
    match_long = len(match_list)
    match = 0
    for i in range(total-match_long+1):
        match = 0
        for j in range(match_long):
            if main[i+j] != match_list[j]:
                match = 1
                break
        if match == 0:
            return 1
    return 0

match_list = [23,0]

def build_lsp(pattern):
    n=len(pattern)
    back_n = [0]*n
    i,length=1,0
    while i<n:
        if pattern[i] == pattern[length]:
            length+=1
            back_n[i]=length
            i+=1
        else:
            if length != 0:
                length = back_n[length-1]
            else:
                back_n[i]=0
                i+=1
    return back_n

def kmp(text,pattern):
    back_n = build_lsp(pattern)
    match = 0
    n,m=len(text),len(pattern)
    i,j=0,0
    while i<n:
        if text[i] == pattern[j]:
            i+=1
            j+=1
            if j==m:
                return i-j
        else:
            if j>0:
                j = back_n[j-1]
            else:
                i+=1
    return -1

lsp=('17762')
text = ('ababaegdjsjnfsljewijvflnjxnzmncnsdndkl17761')
print(kmp(text,lsp))