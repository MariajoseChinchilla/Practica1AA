class Solution:
    def isValid(self, s: str) -> bool:
        read = []
        lookup = {'(': ')', '[': ']', '{': '}'}

        for st in s:
            if st in lookup:
                read.append(st)
            elif len(read) == 0 or lookup[read.pop()] != st:
                return False
        return len(read) == 0
