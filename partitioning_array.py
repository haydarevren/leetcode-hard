#https://leetcode.com/discuss/interview-question/375262/twitter-oa-2019-partitioning-array

def partitioning_array(arr,k):
    n=len(arr)
    if n%k!=0:
        return print('No')
    freqs={}
    for num in arr:
        freqs[num]=freqs.get(num,0)+1
        if freqs[num]>k:
            return print('No')
    r=len(freqs)
    Par_Mat=[[0]*k for i in range(r)]
    i=0
    for freq in freqs.values():
        for j in range(freq):
            Par_Mat[i][j]=1
        i+=1
    print(Par_Mat)
    m=int(n/k)
    summ=0
    for j in range(k):
        for i in range(r):
            summ+=Par_Mat[i][j]
        print(summ,m)
        if summ<m*(j+1):
            return print('Noooo')
    return print('Yes')