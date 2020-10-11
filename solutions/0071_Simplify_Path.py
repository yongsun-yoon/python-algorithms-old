class Solution:
    def simplifyPath(self, path: str) -> str:
        path = path[1:].split('/')
        new_path = []
        
        for p in path:
            # nothing
            if p == '':
                pass
            # now
            elif p == '.':
                pass
            # prev
            elif p == '..':
                if new_path: new_path.pop()
            # subdir
            else:
                # dirname
                new_path.append(p)
            
        return '/' + '/'.join(new_path)