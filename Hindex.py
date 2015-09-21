from collections import Counter

def hindex(citations):
    if not citations:
        return 0
    n=len(citations)
    lower=0
    upper= n-1
    last=0
    while lower<=upper:
        print(citations[lower:upper+1])
        mid=(lower+upper)//2
        if citations[mid]==n-mid:
            return n-mid
        elif citations[mid]<n-mid:
            lower = mid+1
            last=citations[mid]
        else:
            upper = mid-1
            last=citations[mid]
    #print(last)
    #print(n)
    #print(mid)
    if last<n-mid:
        return n-mid-1
    return n-mid

citations=[0,0]
print(hindex(citations))