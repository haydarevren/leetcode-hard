#https://leetcode.com/discuss/interview-question/819577/Throttling-Gateway-Hackerrank

def droppedRequests(requestTime):
    if not requestTime or len(requestTime)==0:
        return 0
    rules=[[10,20],[60,60]] #second and third rule
    D={}
    dropped=[]
    for i in requestTime:
        if i in D:
            if D[i]==3: #first rule
                dropped.append(i)
            else: D[i]+=1 
        else:
            D[i]=1

    maximum=max(D.keys())

    def throttle(dic,drop_list,start,num):
        if num:
            j=0
            while j<start:
                if dic.get(start-j,0):
                    size=min(dic[start-j],num)
                    drop_list.extend([start-j]*size)
                    print(drop_list,size)
                    dic[start-j]-=size
                    num-=size
                    j+=1
                    start-=j
                    return throttle(dic,drop_list,start,num)
                j+=1
            

    for rule in rules:
        cumulative_requests=0
        window=rule[0]
        if window>maximum: continue

        for i in range(window):
            cumulative_requests+=D.get(1+i,0)


        i=0
        
        while i<=maximum-window:
            diff=max(0,cumulative_requests-rule[1])
            throttle(D,dropped,window+i,diff)
            cumulative_requests-=diff
            next_iteration=D.get(1+window+i,0)-D.get(1+i,0)
            cumulative_requests+=next_iteration
            i+=1     
    return len(dropped)





RequestTime = [1,1,1,1,2,2,2,3,3,3,3,4,5,5,5,6,6,6,6,7,7,7,8,8,8,8,9,9,9,9,9,10,10]
print(droppedRequests(RequestTime))