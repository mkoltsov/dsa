class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        len0,len1=0,0
        for i in nums:
            if i==0:
                len0+=1
            elif i==1:
                len1+=1
        return len1+len0        


            
            