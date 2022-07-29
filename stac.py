class Stack:
    def __init__(self):
        self.stack = []

    def size_of_stack(self):#size - size_of_stack
        return len(self.stack)

    def pop_elem(self):#pop - pop_elem
        if len(self.stack) != 0:
            RESULT_ARRAY = self.stack[len(self.stack)-1] # a - RESULT_ARRAY
            del self.stack[len(self.stack)-1]
            return RESULT_ARRAY
        return None # если стек пустой

    def push_elem(self, value):# push - push_elem
        self.stack.insert(len(self.stack),value)
        # ваш код

    def peek_elem(self):#peek - peek_elem
        if len(self.stack) != 0:
            return self.stack[len(self.stack)-1]
        return None # если стек пустой

def balans_in_stack(string):# balans - balans_in_stack
    STACK = Stack() # s - STACK
    for i in string:
        STACK.push_elem(i)
    sum_open = 0
    sum_close = 0
    while STACK.size_of_stack() > 0:
        l = STACK.size
        if STACK.peek_elem() == ")":
            return False
        if STACK.pop_elem() =="(" and STACK.size_of_stack() == 1:
            return False
        if STACK.pop_elem() =="(":
            sum_open +=1
        else:
            sum_close +=1
    if sum_open == sum_close:
        return True
    else:
        return False
