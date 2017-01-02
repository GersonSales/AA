try:
    while 1:
        stack = []
        expression = raw_input()
        valid = True
        for e in  expression:
            if (e == "("):
                stack.append(e)
            elif (e == ")"):
                if (len(stack) != 0 and stack[len(stack) - 1] == "("):
                    stack.pop()
                else:
                    valid = False
                    break
        if (valid and len(stack) == 0):
            print "correct"
        else:
            print "incorrect"
except EOFError:
    pass
