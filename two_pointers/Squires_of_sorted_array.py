# Given an integer array nums sorted in non-decreasing order, 
# return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def get_squires(arr):
        n = len(arr)
        left = 0
        right = n - 1
        squired_arr = [0] * n

        while left <= right:
            left_side = arr[left] ** 2
            right_side = arr[right] ** 2

            #if left_side is bigger take it to the end of the array
            if left_side > right_side:
                squired_arr[n] = left_side
                left += 1
            else:
                squired_arr[n] = right_side
                right -= 1
            
            n -= 1
        
        return squired_arr


