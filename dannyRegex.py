
def isMatch(s, p):
    """
    :type s: str
    :type p: str
    :rtype: bool
    """
    
    def isMatchRec(s,exp):
        
        s_pos=0
        exp_pos=0
        #print("New recursive call")
        #print(s)
        #print(exp)
        #input()
        '''
        if there are no characters left in the input string,
        we test to see if the expression contains only a ** or a .**
        '''
        if len(s)==0:
            if len(exp)==2:
                if exp[0]=="." and exp[1]=="**":
                    return True
            elif len(exp)==1:
                if exp[0]=="**":
                    return True
        '''
        while there are things in both the input string and the expression
        '''
        while s_pos<len(s) and exp_pos<len(exp):
            #print(s[s_pos:])
            #print(exp[exp_pos:])
            #input()

            #get the next token
            curr_token=exp[exp_pos]
            #if its a dot in both string, jump past it
            #otherwise return false
            if curr_token==".":
                if s[s_pos]==".":
                    exp_pos+=1
                    s_pos+=1
                else:
                    return False
            else:
                #if its a non "**" token
                if len(curr_token)==1:
                    # if its a %, jump past it in both string, unless s has a "." in which case fail
                    if curr_token=="%":
                        if s[s_pos]!=".":
                            s_pos+=1
                            exp_pos+=1
                        else:
                            return False
                    #if its a *, then jump past the * and the next . in the regex string
                    #jump to the next . in the input string
                    elif curr_token=="*":
                        s_pos = s.find(".",s_pos)
                        #no more dots, so we match the whole string
                        if s_pos==-1:
                            #set the s_pos pointer to be "done" (caught by the if at the bottom)
                            s_pos = len(s)
                            #move the exp_pos (its possible we have not matched everything, which the if at the bottom will check)
                            exp_pos+=2
                        
                        else:
                            #dots dont need to be matched so move past it in the input string
                            s_pos+=1
                            #get past * and the next . in the regex
                            exp_pos+=2
                    #this is the case where it is just a letter
                    else:
                        if s[s_pos]==curr_token:
                            s_pos+=1
                            exp_pos+=1
                        else:
                            return False
                #the ** case
                else:
                    #choose to match nothing from ** by moving past the ** in the regex, 
                    #but staying in the same place in the input string
                    
                    #print("choose nothing")
                    if isMatchRec(s[s_pos:],exp[exp_pos+2:]):
                        return True
                    #otherwise, chomp dot segements and recurse
                    upcoming_dots  = [i for i,letter in enumerate(s[s_pos:]) if letter == "."]
                    #add the case where the ** matches everything (since there is no trailing .)
                    upcoming_dots.append(len(s[s_pos:]))
                    #print(s[s_pos:])
                    #print("dot_pos",upcoming_dots)

                    #for each upcoming dot, process everything before it and recurse
                    for dot_pos in upcoming_dots:
                        #print("choose to chomp until",dot_pos)
                        if isMatchRec(s[dot_pos+1:],exp[exp_pos+2:]):
                            return True
                    #if none of those possibilities matched, we are done
                    return False
        # if both are pointers have passed the ends of the strings, we are done
        if s_pos>=len(s) and exp_pos >=len(exp):
            return True
        return False

    
    exp=[]
    i=0
    while i < len(p):
        if p[i]=="*":
            if i+1<len(p):
                if p[i+1]=="*":
                    exp.append("**")
                    i+=1
                else:
                    exp.append("*")
            else:
                exp.append("*")
        else:
            exp.append(p[i])
        i+=1
    #print(exp)
    return isMatchRec(s,exp)
    


print(isMatch("abc","abc.**"))
