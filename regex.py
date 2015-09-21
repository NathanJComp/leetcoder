class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """
        
        def isMatchRec(s,exp):
            print(s)
            print(exp)
            input()
            s_pos=0
            exp_pos=0
            if len(s)==0:
                if min(len(x))==2 for x in exp_pos:
                    return True
                return False
            while s_pos<len(s) and exp_pos<len(exp):
                curr_token=exp[exp_pos]
                if len(curr_token)==1:
                    if curr_token==".":
                        s_pos+=1
                        exp_pos+=1
                    else:
                        if s[s_pos]==curr_token:
                            s_pos+=1
                            exp_pos+=1
                        else:
                            return False
                else:
                    #if we want nothing from the *
                    if s[s_pos]!=curr_token[0]:
                        exp_pos+=1
                    else:
                        #choose to match nothing from *
                        if isMatchRec(s[s_pos:],exp[exp_pos+1:]):
                            return True
                        while s[s_pos]==curr_token[0]:
                            if isMatchRec(s[s_pos+1:],exp[exp_pos:]):
                                return True

                        return False
            if s_pos==len(s) and exp_pos ==len(exp):
                return True
            return False


        exp=[]
        for c in p:
            if c=="*":
                exp[-1]=exp[-1]+c
            else:
                exp.append(c)
        return isMatchRec(s,exp)
            
            
a=Solution

print(a.isMatch(a,"aa","a*"))