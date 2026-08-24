class Solution:
    def romanToInt(self, s: str) -> int:
        t = len(s)
        romanos = {
            'M':1000, 'D':500,'C':100,'L':50,'X':10,'V':5,'I':1
        }
        a = 0
        i = 0
        for i in range(0,t-1):
            if romanos[s[i]] < romanos[s[i+1]]: a -= romanos[s[i]]
            else: a += romanos[s[i]]
        a += romanos[s[-1]]
        return a

Solution.romanToInt(Solution, 'IV')