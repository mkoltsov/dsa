def find_length(nums:str)->int:
    ans,curr=0,0
    right, left=0,0
    for right in range(len(nums)):
        if nums[right]=="0":
            curr+=1
        while curr>1:
            if nums[left]=="0":
                curr-=1
            left+=1    
        print(right)
        ans=max(ans,right-left+1)
        print(f"{ans=}, {left=}, {right=}") 
    return ans

print(find_length("1101100111"))            