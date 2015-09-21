nums=[0,3,4,0]
target=0
def sum_pair(nums,target):
    nums_with_pos = {}
    for i,x in enumerate(nums):
        nums_with_pos.setdefault(x,[])
        nums_with_pos[x].append(i)
    print(nums_with_pos)
    for num in nums_with_pos:
        if target-num in nums_with_pos:
            first_pos=nums_with_pos[num][0]
            for second_pos in nums_with_pos[target-num]:
                if first_pos+1<second_pos+1:
                    return (first_pos+1,second_pos+1)
                elif first_pos+1>second_pos+1:
                    return (second_pos+1,first_pos+1)
print(sum_pair(nums,target))