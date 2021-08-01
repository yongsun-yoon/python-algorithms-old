from typing import List

class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        visits = {}
        
        for cpd in cpdomains:
            cnt, cpd = cpd.split(' ')
            cpd = cpd.split('.')
            
            for i in range(len(cpd)):
                sub = '.'.join(cpd[i:])
                visits.setdefault(sub, 0)
                visits[sub] += int(cnt)
        
        return [str(v) + ' ' + k for k,v in visits.items()]