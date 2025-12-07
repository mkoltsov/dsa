from collections import defaultdict
class Solution:
    def largestUniqueNumber(self, nums: List[int]) -> int:
        num=defaultdict(int)
        for i in nums:
            num[i] +=1
        # val=0
        ans=-1
        print(num)
        for k,v in num.items():
            if v==1:
                print(f"{k} - {v}")
                ans=max(ans,k)
                print(ans)

        return ans

print(Solution().largestUniqueNumber([5,7,3,9,4,9,8,3,1]))             