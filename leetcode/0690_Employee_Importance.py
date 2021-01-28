from typing import List

"""
# Definition for Employee.
class Employee:
    def __init__(self, id: int, importance: int, subordinates: List[int]):
        self.id = id
        self.importance = importance
        self.subordinates = subordinates
"""

class Solution:
    def getImportance(self, employees: List['Employee'], id: int) -> int:
        employees = {i.id:i for i in employees}
        group = [id]
        ans = 0
        while group:
            id = group.pop(0)
            em = employees[id]
            group += em.subordinates 
            ans += em.importance
        return ans