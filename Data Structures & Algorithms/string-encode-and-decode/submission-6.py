class Solution:

    def encode(self, strs: List[str]) -> str:
        return "\t".join(strs) if strs else "\t"

    def decode(self, s: str) -> List[str]:
        return s.split("\t") if s is not "\t" else []