def prefix(nums:List[int]) -> List[int]:
    prefix=[nums[0]]
    for i in range(1, len(nums)):
        prefix.append(nums[i]+prefix[-1])
    return prefix

print(prefix([5, 2, 1, 6, 3, 8]))
