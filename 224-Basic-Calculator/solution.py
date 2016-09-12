class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        def parseString(s):
            # parse input string into infix expression
            infix = []
            i = 0
            while i < len(s):
                if s[i] == ' ':
                    i += 1
                    continue
                elif s[i] in '()*/+-':
                    infix.append(s[i])
                    i += 1
                else:
                    num = 0
                    while i < len(s) and '0' <= s[i] <= '9':
                        num = 10 * num + int(s[i])
                        i += 1
                    infix.append(str(num))
                
            return infix
            
        def precedence(token):
            if token in '*/':
                return 2
            elif token in '+-':
                return 1
            elif token == '(':
                return 0
        
        def convert2RPN(infix):
            opStack = []
            rpn = []
            for elem in infix:
                if elem == '(':
                    opStack.append(elem)
                elif elem == ')':
                    while opStack[-1] != '(':
                        rpn.append(opStack.pop())
                    opStack.pop()
                elif elem in '*/+-':
                    while opStack and precedence(opStack[-1]) >= precedence(elem):
                        rpn.append(opStack.pop())
                    opStack.append(elem)
                else:
                    rpn.append(elem)
                
            while opStack:
                rpn.append(opStack.pop())
            return rpn
            
        def evalRPN(postfix):
            vals = []
            for elem in postfix:
                if elem in '+-*/':
                    val1 = vals.pop()
                    val2 = vals.pop()
                    if elem == '+':
                        vals.append(val1 + val2)
                    elif elem == '-':
                        vals.append(val2 - val1)
                    elif elem == '*':
                        vals.append(val1 * val2)
                    else:
                        vals.append(val2 / val1)
                else:
                    vals.append(int(elem))
            return vals[0]
        
        
        infix = parseString(s)
        rpn = convert2RPN(infix)
        val = 0
        if rpn:
            val = evalRPN(rpn)
        return val
        
                     
        