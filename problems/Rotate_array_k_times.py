# Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
# Example 1:

# Input: nums = [1,2,3,4,5,6,7], k = 3
# Output: [5,6,7,1,2,3,4]
# Explanation:
# rotate 1 steps to the right: [7,1,2,3,4,5,6]
# rotate 2 steps to the right: [6,7,1,2,3,4,5]
# rotate 3 steps to the right: [5,6,7,1,2,3,4]
# Example 2:

# Input: nums = [-1,-100,3,99], k = 2
# Output: [3,99,-1,-100]
# Explanation: 
# rotate 1 steps to the right: [99,-1,-100,3]
# rotate 2 steps to the right: [3,99,-1,-100]

def reverse(arr, left, right): #reverse the array first

    while left < right:
        ar[left], arr[right] = arr[right], arr[left]
        left += 1
        right -= 1

def solution(arr, k):
    n = len(arr)

    k = k % n #to find out the maximum rotation needed

    reverse(arr, 0, n - 1) #first we are reversing the entire array
    reverse(arr, 0, k - 1) #than we are reversein the first k elenents
    reverse(arr, k, n - 1) #than we reverse the rest of the elements form k

    return arr
