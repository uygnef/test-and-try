min_stack = []
stack = []

def pop():
    if (not stack) or (not min_stack):
        raise "Stack is empty"
    if min_stack[-1] == min_stack[-1]:
        min_stack.pop()
    stack.pop()

def push(num):
    stack.append(num)
    if not min_stack:
        min_stack.append(num)
        return
    if num <= min_stack[-1]:
        min_stack.append(num)

def min():
    if not min_stack:
        return None
    return min_stack[-1]


