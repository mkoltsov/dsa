def twoSum(nums: List[int], target: int) -> List[int]:
    res={}
    for i in range(len(nums)):
        num=nums[i]
        con=target-num
        if con in res:
            return [i, res[con]]
        res[num]=i

print(twoSum([5,2,7,10,3,9],8))        