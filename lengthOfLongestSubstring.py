# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.next = None
import string
def lengthOfLongestSubstring(s):
        current_start=0
        pos_dict={}
        longest=0
        for ind,c in enumerate(s):
            if c in pos_dict:
                #if we have seen this letter in the current substring
                if pos_dict[c]>=current_start:
                    if ind-current_start>longest:
                        longest=ind-current_start
                    current_start=pos_dict[c]+1
            pos_dict[c]=ind
        if len(s)-current_start>longest:
            longest = len(s)-current_start
        return longest



print(lengthOfLongestSubstring(input()))