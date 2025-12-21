# Problem: Valid Parentheses
# Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.
# An input string is valid if:
# Open brackets must be closed by the same type of brackets.
# Open brackets must be closed in the correct order.
# Every close bracket has a corresponding open bracket of the same type.

def is_valid_parentheses_v1(parentheses_str):
    stack = []
    opening = ['(', '{', '[']
    closing = [')', '}', ']']
    for p in parentheses_str:
        if p in opening:
            stack.append(p)
        else:
            if not stack:
                return False
            last_in_stack = stack.pop()
            index1 = opening.index(last_in_stack)
            index2 = closing.index(p)
            if index1 != index2:
                return False
    return len(stack) == 0

def is_valid_parentheses(parentheses_str):
    stack = []
    match = {'(': ')', 
             '{': '}',
             '[':']'}
    for p in parentheses_str:
        if p in match:
            stack.append(p)
        else:
            if not stack:
                return False
            last_in_stack = stack.pop()
            if match.get(last_in_stack) != p:
                return False
    return len(stack) == 0




print(is_valid_parentheses("()"))        # True
print(is_valid_parentheses("{[()]}"))    # True
print(is_valid_parentheses("([)]"))      # False
print(is_valid_parentheses(")()"))       # False