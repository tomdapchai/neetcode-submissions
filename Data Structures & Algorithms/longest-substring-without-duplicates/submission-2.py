class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        hash_map = defaultdict(lambda: -1)
        count, tmp = 0, 0
        i, j = 0, 0
        while j < len(s):
            v = hash_map[s[j]]
            if v == -1 or (v >= 0 and v < i):
                tmp += 1
            else:
                count = max(tmp, count)
                i = v + 1
                tmp = j - i + 1
            hash_map[s[j]] = j
            j += 1
        
        count = max(tmp, count)
        return count

