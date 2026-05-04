#Given two sorted integer arrays arr1 and arr2, 
# return a new array that combines both of them and is also sorted.

def array(num1, num2):
    ans = []
    i = j = 0

    while i < len(num1) and j < len(num2):
        if num1[i] < num2[j]:
            ans.append(num1[i])
            i += 1
        else:
            ans.append(num2[j])
            j += 1
    
    while i < len(num1):
        ans.append(num1[i])
        i ++ 1
    
    while j < len(num2):
        ans.append(num2[j])
        j += 1
    
    return ans

