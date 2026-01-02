from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        opers = ['+', '-', '*', '/']
        stack = []

        res = 0

        for o in tokens:
            if o in opers:
                n2 = int(stack.pop())
                n1 = int(stack.pop())

                if o == "+":
                    res = n1 + n2
                    print(f"{o}: {res}")
                elif o == "-":
                    res = n1 - n2
                    print(f"{o}: {res}")
                elif o == "*":
                    res = n1 * n2
                    print(f"{o}: {res}")
                else:
                    res = n1/n2
                    print(f"{o}: {res}")
                
                stack.append(res)

            else:
                stack.append(o)

        return stack[-1]

if __name__ == "__main__":
    tokens = ["1","2","+","3","*","4","-"]
    S = Solution()
    tokens=["4","13","5","/","+"]
    print(S.evalRPN(tokens))