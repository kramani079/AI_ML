# Create an empty stack
stack = []

# PUSH operation
def push(item):
    stack.append(item)
    print(f"{item} pushed into stack")

# POP operation
def pop():
    if len(stack) == 0:
        print("Stack is empty")
    else:
        removed = stack.pop()
        print(f"{removed} popped from stack")

# Demonstration
push(10)
push(20)
push(30)

print("Stack after push operations:", stack)

pop()
pop()

print("Stack after pop operations:", stack)
