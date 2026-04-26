#Using a stack to check whether an expression has balanced parentheses.

def check_balanced(expression):
    stack = []
    brackets = {')': '(', '}': '{', ']': '['}
    
    for char in expression:
        if char in '({[':
            stack.append(char)
        elif char in ')}]':
            if not stack or stack.pop() != brackets[char]:
                return "Not Balanced"
    return "Balanced" if not stack else "Not Balanced"

# Test the function
if __name__ == "__main__":
    expr1 = "(a+b)*(c+d)"
    expr2 = "(a+b)*(c+d"
    expr3 = "{[()]}"
    expr4 = "{[(])}"
    
    print(f"{expr1}: {check_balanced(expr1)}")
    print(f"{expr2}: {check_balanced(expr2)}")
    print(f"{expr3}: {check_balanced(expr3)}")
    print(f"{expr4}: {check_balanced(expr4)}")
