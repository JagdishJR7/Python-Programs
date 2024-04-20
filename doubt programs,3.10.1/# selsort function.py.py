def selsort(list,n):
    j=n-1
    while j>0:
        large=list[0]
        index=0
        for i in range(1,j+1):
            if list[i]>large:
                large=list[i]
                index=i
        list[index]=list[j]
        list[j]=large
        j=-1
                
