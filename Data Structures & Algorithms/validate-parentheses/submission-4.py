class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()

        for c in s:
            if c == '[' or c == '(' or c == '{':
                stack.append(c)
                continue
            
            if len(stack) == 0:
                return False
            
            match c:
                case ']':
                    if stack.pop() != '[':
                        return False
                case ')':
                    if stack.pop() != '(':
                        return False
                case '}':
                    if stack.pop() != '{':
                        return False

        if len(stack) != 0:
            return False

        return True