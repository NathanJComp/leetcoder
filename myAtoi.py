def myAtoi(str):
    if str=="":
        return 0
    sign=1
    pos=0
    while str[pos]=="+" or str[pos]=="-":
        if str[pos]=="-":
            sign*=-1
        pos+=1
    try:
        return int(str[pos:])*sign
    except ValueError:
        return "String must contain a seq of +,- followed by an integer"
print(myAtoi("+---2"))