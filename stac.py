class Stack:
    def __init__(self):
        self.stack = []

    def size(self):
        return len(self.stack)

    def pop(self):
        if len(self.stack) != 0:
            a = self.stack[len(self.stack)-1]
            del self.stack[len(self.stack)-1]
            return a
        return None # если стек пустой

    def push(self, value):
        self.stack.insert(len(self.stack),value)
        # ваш код

    def peek(self):
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
        return None # если стек пустой

def balans(string):
    stack = Stack()
    for i in string:
        stack.push(i)
    sum_open = 0
    sum_close = 0
    while stack.size() > 0:
        l = stack.size
        if stack.peek() == ")":
            return False
        if stack.pop() =="(" and stack.size() == 1:
            return False
        if stack.pop() =="(":
            sum_open +=1
        else:
            sum_close +=1
    if sum_open == sum_close:
        return True
    else:
        return False