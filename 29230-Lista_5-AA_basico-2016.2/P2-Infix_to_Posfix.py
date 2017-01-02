n = int(raw_input())

operators = "-+*/^"

for i in xrange(n):
    expression = list(raw_input())
    
    index = 0;

    while index < len(expression):
        if (expression[index] in operators):
            aux = expression[index]
            expression[index] = expression[index + 1]
            expression[index + 1] = aux
            index += 1
        elif(expression[index] in "()[]{}"):
            del expression[index]
            index -= 1

        index += 1

    print "".join(expression)
