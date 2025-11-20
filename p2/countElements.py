class Solution:
    def countElements(self, arr: List[int]) -> int:
        unique=set(arr)
        num=0
        for i in arr:
            if i+1 in arr:
                num+=1
        return num        