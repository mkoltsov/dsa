from typing import List
def numsubarrayproductlessthank(nums:List[int], k:int)->int:
    if k<=1:
        return 0
    left, right, curr, ans=0,0,1,0
    for right in range(len(nums)):
        curr*=nums[right]
        while curr>=k:
            curr//=nums[left]
            left+=1
        ans+=right-left+1    
    return ans
print(numsubarrayproductlessthank([10, 5, 2, 6], 100))
