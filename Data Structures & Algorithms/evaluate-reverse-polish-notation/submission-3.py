class Solution:
    def add(self, a, b):
        return a + b
    
    def subtract(self, a, b):
        return a - b
    
    def multiply(self, a, b):
        return a * b
    
    def divide(self, a, b):
        return int(a/b)
    
    def is_number(self, s):
        try:
            float(s)
            return True
        except ValueError:
            return False

    def evalRPN(self, tokens: List[str]) -> int:
        if len(tokens) <= 2:
            return int(tokens[0])
        
        num_list = [int(tokens[0])]
        op = []
        token_len = len(tokens)
        idx = 1

        while idx < token_len:
            val = tokens[idx]
            if self.is_number(val):
                num_list.append(int(val))
            else:
                num2 = num_list.pop()
                num1 = num_list.pop()
                op = tokens[idx]
        
                if op == '+':
                    res = self.add(num1, num2)
                elif op == "-":
                    res = self.subtract(num1, num2)
                elif op == "*":
                    res = self.multiply(num1, num2)
                else:
                    res = self.divide(num1, num2)
                
                num_list.append(res)
            
            idx += 1
        
        return num_list[0]


