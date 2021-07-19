class Solution:
    def maxLengthBetweenEqualCharacters(self, s: str) -> int:
        char_idx = {}
        for idx, char in enumerate(s):
            char_idx.setdefault(char, [])
            char_idx[char].append(idx)
        
        ans = []
        for k, v in char_idx.items():
            if len(v) < 2:
                continue
            ans.append(max(v) - min(v) - 1)
        
        return max(ans) if ans else -1
