class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        for char in s:
            if ((char == '(') or (char == '{') or (char == '[')):
                stack.append(char)
            elif ((char == ')') or (char == '}') or (char == ']')):
                if stack == [] :
                    return False
                top = stack[-1]
                if ((char == ')' and top != '(') or (char == '}' and top != '{') or (char == ']' and top != '[')):
                    return False
                stack.pop()
        if stack==[]:
            return True
        else:
            return False
        
