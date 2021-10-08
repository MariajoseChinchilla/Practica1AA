class Solution:
    def isAnagram(self,s,t):
        if len(s) != len(t):
            return False
        else:
            for letter in t:
                if letter not in s:
                    break
                    return False
                else:
                    s = s.replace(letter,'',1)
                    t = t.replace(letter,'',1)
                    if s == '':
                        return True