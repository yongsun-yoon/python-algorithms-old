class Solution:
    def reformatDate(self, date: str) -> str:
        month = ["Jan", "Feb", "Mar", "Apr", "May", "Jun", "Jul", "Aug", "Sep", "Oct", "Nov", "Dec"]
        d, m, y = date.split(' ')
        m = str(month.index(m) + 1).zfill(2)
        d = d[:sum([_d.isnumeric() for _d in d])].zfill(2)
        return f'{y}-{m}-{d}'