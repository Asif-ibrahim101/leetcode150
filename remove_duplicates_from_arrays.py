# Given an integer array nums sorted in non-decreasing order, 
# remove the duplicates in-place such that each unique element appears only once. 
# The relative order of the elements should be kept the same.

# Consider the number of unique elements in nums to be k​​​​​​​​​​​​​​. 
# After removing duplicates, return the number of unique elements k.

# The first k elements of nums should contain the unique numbers in sorted order. 
# The remaining elements beyond index k - 1 can be ignored.

def remove_duplicates(nums):
    n = len(nums)

    if not nums:
        return 0

    k = 1 #number of uniqe elements

    for x in range(1, n):
        if nums[x] != nums[ x - 1]:
            nums[k] = nums[x]
            k += 1
    
    return k

arr = [1,2,2,3,4]
answer = remove_duplicates(arr)
print(answer)