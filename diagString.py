def diag_string(s,numRows):
    """
    :type s: str
    :type numRows: int
    :rtype: str
    """
    if numRows==1:
        return s
    ret=""
    for row in range(numRows):
        if row==0:
            pos=0
            while pos<len(s):
                ret+=s[pos]
                pos+=2*numRows-2
        elif row==numRows-1:
            pos=numRows-1
            while pos<len(s):
                ret+=s[pos]
                pos+=2*numRows-2
        else:
            pos=row
            print(pos)
            while pos<len(s):
                ret+=s[pos]
                pos+=2*numRows-2-2*row
                print(pos)
                if pos<len(s):
                    ret+=s[pos]
                    pos+=2*row
                    print(pos)
                
    return ret
print(diag_string("", 1))