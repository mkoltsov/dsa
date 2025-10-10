from typing import List

def find_size(nums:List[int], k:int)->int:
    left, right, curr, ans=0,0,0,0
    for right in range(len(nums)):
        curr+=nums[right]
        while curr>k:
            curr-=nums[left]
            left+=1
        ans=max(ans,right-left+1)
    return ans


print(find_size( [3, 1, 2, 7, 4, 2, 1, 1, 5], 8))