class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []

        for i in range(len(tokens)):
            cal = None
            if  tokens [i] == "+" or tokens[i] == "-" or tokens[i] == "*" or tokens[i] == "/":
                
                if tokens[i] == "+":
                    cal = stack.pop()  + stack.pop()
                elif tokens[i] == "-":
                    left_el = stack.pop()

                    right_el = stack.pop()
                    
                    cal = right_el - left_el
                elif tokens[i] == "*":
                    cal = stack.pop() * stack.pop()
                else:
                    left_el = stack.pop()

                    right_el = stack.pop()
                    
                    cal = right_el / left_el

                stack.append(int(cal))
            else:
                stack.append(int(tokens[i]))
        #print("2 - 3 =",2-3, "3-2 = ", 3 -2)
        return stack[0]

        