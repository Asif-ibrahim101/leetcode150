# You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, 
# and two integers m and n, representing the number of elements in nums1 and nums2 respectively.
# Merge nums1 and nums2 into a single array sorted in non-decreasing order.
# The final sorted array should not be returned by the function,
#  but instead be stored inside the array nums1. To accommodate this, nums1 has a length of m + n, 
# where the first m elements denote the elements that should be merged, and the last n elements are set to 0 and should be ignored. nums2 has a length of n.

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int): 
        pointer1 = m - 1
        pointer2 = n - 1
        pointer_last = m + n -1

        while pointer2 >= 0:
            if pointer1 >= 0 and nums1[pointer1] > nums2[pointer2]:
                nums1[pointer_last] = nums1[pointer1]
                pointer1 -= 1
            else:
                nums1[pointer_last] = nums2[pointer2]
                pointer2 -= 1
            
            pointer_last -= 1
        
        return pointer1
