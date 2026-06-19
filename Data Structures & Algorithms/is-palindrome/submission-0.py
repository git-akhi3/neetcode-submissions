class Solution:
    def isPalindrome(self, s: str) -> bool:
        cs = ''.join(c.lower() for c in s if c.isalnum())
        left = 0 
        right = len(cs) -1

        while right > left :
            if cs[left] != cs[right]:
                return False
            
            left += 1
            right -= 1
            
        return True
