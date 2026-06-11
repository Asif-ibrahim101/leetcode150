# 1456. Maximum Number of Vowels in a Substring of Given Length
# Given a string s and an integer k, return the maximum number of vowel letters in any substring of s with length k.

# Vowel letters in English are 'a', 'e', 'i', 'o', and 'u'.
# Example 1:

# Input: s = "abciiidef", k = 3
# Output: 3
# Explanation: The substring "iii" contains 3 vowel letters.
# Example 2:

# Input: s = "aeiou", k = 2
# Output: 2
# Explanation: Any substring of length 2 contains 2 vowels.

def Solution(s, k):
    n = len(s)
    left = 0
    answer = 0
    counter = 0
    vowels = set("aeiou")

    for right in range(n):
        if s[right] in vowels:
            counter += 1
        
        if right - left + 1 == k:
            answer = max(answer, counter)

            if s[left] in vowels:
                counter -= 1
            
            left += 1
    
    return answer
        