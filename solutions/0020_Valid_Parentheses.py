class Solution:
    def isValid(self, s: str) -> bool:
        opened = ['(', '{', '[']
        closed = [')', '}', ']']
        status = []
        
        for _s in s:
            if _s in opened:
                status.append(_s)

            elif _s in closed:
                if len(status) == 0:
                    return False
                else:
                    index = opened.index(status.pop())
                    if closed.index(_s) != index:
                        return False
            else:
                pass
        
        return True if len(status) == 0 else False
        