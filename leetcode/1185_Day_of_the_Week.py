from datetime import datetime

class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        weekdays = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        year, month, day = str(year), str(month).zfill(2), str(day).zfill(2)
        dt = datetime.strptime(f'{year}{month}{day}', '%Y%m%d')
        ans = weekdays[dt.weekday()]
        return ans