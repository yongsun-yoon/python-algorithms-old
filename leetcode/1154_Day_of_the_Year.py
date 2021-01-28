from datetime import datetime, timedelta

class Solution:
    def dayOfYear(self, date: str) -> int:        
        date = datetime.strptime(date, '%Y-%m-%d')
        first = datetime(date.year, 1, 1)
        diff = (date - first).days + 1
        return diff