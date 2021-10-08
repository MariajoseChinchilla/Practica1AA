class Solution:
    def firstUniqChar(self,s):
        chars = set(s)
        copystring = s
        for char in chars:
            s = s.replace(char,'',1)
        else:
            for letter in copystring:
                if letter not in s:
                    return copystring.index(letter)
            for sym in s:
                if sym in copystring:
                    return -1