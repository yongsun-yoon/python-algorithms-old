from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 0:
            return ''
        
        strs = [list(i) for i in strs]
        prefix = ''

        while True:
            for i in range(len(strs)):
                _str = strs[i]
                if len(_str) > 0:
                    if i == 0:
                        _prefix = _str.pop(0)
                    else:
                        if _prefix != _str.pop(0):
                            return prefix
                else:
                    return prefix
 
                
            prefix += _prefix
        return prefix