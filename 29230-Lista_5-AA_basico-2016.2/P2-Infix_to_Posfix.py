import string
class Stack:
    def __init__(self):
        self.items = []

    def isEmpty(self):
        return self.items == []

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop()

    def peek(self):
        return self.items[len(self.items) - 1]

    def size(self):
        return len(self.items)

    def __str__(self):
        return str(self.items)




def infixToPostfix(expression = ""):
    expression = "".join(expression.split())
    priority = {"^": 3, "*": 2, "/": 2, "+": 1, "-": 1}
    symbols = string.ascii_uppercase
    symbols += string.ascii_lowercase
    symbols += string.digits

    stack = Stack()
    postfix = []

    for term in expression:

        if (term in symbols):
            postfix.append(term)
        elif (priority.has_key(term)):
            if (stack.isEmpty()):
                stack.push(term)
            else:
                peek = stack.peek()
                if (priority.has_key(peek)):
                    if (priority[term] > priority[peek]):
                        stack.push(term)
                    else:
                        postfix.append(stack.pop())
                        peek = stack.peek()
                        while (priority.has_key(peek) and priority[term] <= priority[peek]):
                            postfix.append(stack.pop())
                            peek = stack.peek()

                        stack.push(term)
                else:
                    stack.push(term)

        else:
            if (term == "("):
                stack.push(term)
            elif (term == ")"):
                peek = stack.peek()
                while (peek != "("):
                    postfix.append(stack.pop())
                    peek = stack.peek()
                if (peek == "("):
                    stack.pop()
    return "".join(postfix)


for i in xrange(int(raw_input())):
    print infixToPostfix("(" + raw_input() + ")")






































