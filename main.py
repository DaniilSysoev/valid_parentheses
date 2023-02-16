class Solution:
    def isValid(self, s: str) -> bool:
        brackets = {')': '(', ']': '[', '}': '{'}
        line = []
        for i in s:
            if line == [] or i in list(brackets.values()):
                line.append(i)
            elif line[-1] == brackets[i]:
                line.pop()
            else:
                return False
        return False if len(line) != 0 else True