class Solution:
    def romanToInt(self, s: str) -> int:
        roman_dict = {
            'I' : 1,
            'V' : 5,
            'X' : 10,
            'L' : 50,
            'C' : 100,
            'D' : 500,
            'M' : 1000
        }
        
        prev, total = 0, 0
        for _s in s:
            val = roman_dict[_s]
            if val > prev:
                total -= prev
            else:
                total += prev
            prev = val
        
        total += prev
        return total