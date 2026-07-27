class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        hashmap = defaultdict(list)
        for s in strs:
            merge = "".join(sorted(s))
            hashmap[merge].append(s)
        
        return [hashmap[item] for item in hashmap]
