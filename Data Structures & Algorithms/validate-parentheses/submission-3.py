class Solution:
    def isValid(self, s: str) -> bool:
        open = ['(', '{', '[']
        close = {')': '(', '}': '{', ']': '['}

        stack = []

        for char in s:
            if char in open:
                stack.append(char)
            elif len(stack) != 0 and close[char] == stack[-1]:
                stack.pop()
            else:
                return False

        return len(stack) == 0