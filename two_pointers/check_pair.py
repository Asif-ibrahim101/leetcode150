# Example 2: Given a sorted array of unique integers and a target integer, 
# return true if there exists a pair of numbers that sum to target, false otherwise. 
# This problem is similar to Two Sum. (In Two Sum, the input is not sorted).
# For example, given nums = [1, 2, 4, 6, 8, 9, 14, 15] and target = 13, 
# return true because 4 + 9 = 13.

def check_pair(arr, target):
    n = len(arr)
    left = 0
    right = n - 1

    while left < right:
        curr_sum = arr[left] + arr[right]

        if curr_sum == target:
            return True
        elif current_sum < target:
            left += 1  # Need larger sum, move left forward
        else:
            right -= 1  # Need smaller sum, move right backward
    return False