class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        n=len(nums)
        prefix=[0]*(n+1)
        averages = [-1] * n
        for i in range(n):
            prefix[i+1]=prefix[i]+nums[i]

        for i in range(k,n-k):
            left,right=i-k, i+k
            subArraySum=prefix[right+1]-prefix[left]
            average=subArraySum//(2*k+1)
            averages[i]=average

        
        print(nums)
        print(prefix)
        return averages  