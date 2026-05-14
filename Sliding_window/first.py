#when the size is fixed like
# “Find max sum of subarray of size k”
# “Average of subarrays of size k”
# “Maximum vowels in substring of length k”
# “Permutation in String” sometimes uses fixed size because window size = length of pattern

# def fixed_size(arr, k):
#     left = 0
#     window_size = 0
#     n = len(arr)

#     for right in range(n):
#         window_size += arr[right]

#         #write the condition according to the question
#         if right - left + 1 == k:
#             ans = max(ans, window_size)
#             window_size -= arr[left]
#             left += 1  
        
#     return ans

#Variable size window "At most K"
# longest substring with at most k distinct characters
# longest subarray with at most k zeros
# maximum fruits in two baskets
# longest repeating character replacement
# subarrays with at most k something
