min_stack = []
stack = []

def pop():
    if (not stack) or (not min_stack):
        raise ValueError("Stack is empty")
    if stack[-1] == min_stack[-1]:
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

a = [1, 2, 3, 4,7,0,-1,23,43,-1,-2,2,0]

for i in a:
    push(i)
print(stack, min_stack)
for i in a:
    pop()
    print(min())