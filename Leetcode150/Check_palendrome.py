# A phrase is a palindrome if, after converting all uppercase letters into lowercase letters and removing all non-alphanumeric characters, it reads the same forward and backward. Alphanumeric characters include letters and numbers.

# Given a string s, return true if it is a palindrome, or false otherwise.

def Check_palendrome(str):
    n = len(str)
    left = 0
    right = n - 1

    while left < right:
        if not str[left].isalnum():
            left+= 1
            continue
        if not str[right].isalnum():
            right -= 1
            continue

        #if the left and right is not equal than we know that the string is not a pallendrome
        if str[left].lower() != str[right].lower():
            return False
        
        left += 1
        right -= 1
    
    return True