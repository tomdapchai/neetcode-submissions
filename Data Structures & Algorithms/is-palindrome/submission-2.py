class Solution:
    def isPalindrome(self, s: str) -> bool:
        # pre process:
        if s == "":
            return True
        strip_s = ""
        for c in s:
            c = c.lower()
            if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9'):
                strip_s += c
        print(strip_s)
        for i in range(len(strip_s) // 2):
            print(i)
            if strip_s[i] != strip_s[len(strip_s) - 1 - i]:
                return False
        
        return True


        