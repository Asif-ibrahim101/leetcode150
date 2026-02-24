def solution(nums):
    n = len(nums)
    p1 = 0

    for p2 in range(1, n):
        if nums[p1] != nums[p2]:
            p1 += 1
            nums[p1] = nums[p2]
        
    return p1 + 1
