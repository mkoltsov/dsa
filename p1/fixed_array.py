from typing import List
def fixed_array (nums:List[int], k:int)->int:
    curr=0
    for i in range(len(nums)):
        curr+=nums[i]
    ans=curr
    for i in range(k, len(nums)):    
        curr+=nums[i]-nums[i-k]
        ans=max(ans,curr)
    return ans

print(fixed_array([1,2,3,4,5],2))
