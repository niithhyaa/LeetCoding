class Solution:
    def isPalindrome(self, x: int) -> bool:
        rev_half = 0
        if (x<0) or (x%10 == 0 and x!=0):
            return False
        while x > rev_half:
            rev_half = rev_half*10 + x%10
            x = x//10
        return (x == rev_half) or (x == rev_half//10)
