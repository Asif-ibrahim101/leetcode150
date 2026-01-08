#Given an array nums of size n, return the majority element.
#The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.

# Input: nums = [3,2,3]
# Output: 3
# Example 2:

# Input: nums = [2,2,1,1,1,2,2]
# Output: 2


#using sorting to solve the problem
# def Solution(nums):
#     nums.sort()
#     n = len(nums)

#     return nums[n // 2]

#using Boyer–Moore Voting Algorithm to solve it this is the most oprtimal solution to find majority element
#what if the majority of the element is not garuntee
def Solution(nums):
    
    count = 0
    candidate = 0

    for num in nums:
        #setting the current_elemt to candidate
        if count == 0:
            candidate = num
        
        #if the currrent_element is same as candiadate increment the counter
        if candidate == num:
            count += 1
        else:
            #if not than decrease the counter
            count -= 1

    
    #verifying if the majority element exits or not
    if nums.count(candidate) > len(nums // 2):
        return candidate
    
    #than we return the majority element
    return None