class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        if len(s) != len(pattern): 
            return False

        mapping = set(zip(pattern, s))
        return len(set(s)) == len(set(pattern)) == len(mapping)
