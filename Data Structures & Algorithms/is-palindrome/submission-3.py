class Solution:
    def isPalindrome(self, s: str) -> bool:
        if s == "":
            return True
        def check(c: str):
            return True if (c >= 'a' and c <= 'z') or (c >= '0' and c <= '9') else False
        s = list(s)
        l, r = 0, len(s) - 1
        while l < r:
            s[l] = s[l].lower()
            s[r] = s[r].lower()
            if not check(s[l]):
                l += 1
            if not check(s[r]):
                r -= 1
            if check(s[l]) and check(s[r]):
                if s[l] != s[r]:
                    return False
                l += 1
                r -= 1
        
        return True


        