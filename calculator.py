class Calculator:
     # wrong code
    # def add(self, a, b):
    #     return a + b

    def add(self,a,b):
        result = a + b
        return result
    # wrong code
    # def subtract(self, a, b):
    #     return b - a

    def subtract(self,a,b):
        result = a - b
        return result
    
     # wrong code
    # def multiply(self, a, b):
    #     result = 0
    #     for i in range(b+1):
    #         result = self.add(result, a)
    #     return result

    def multiply(self,a,b):
        if (b > 0):
            result = 0
            for i in range (b):
                result += a
            return result
        elif (b < 0):
            result = 0
            for i in range (b*-1):
                result -= a
            return result
        elif (b == 0):
            return 0
        else :
            return None
    # wrong code
    # def divide(self, a, b):
    #     result = 0
    #     while a > b:
    #         a = self.subtract(a, b)
    #         result += 1
    #     return result

    def divide(self, a, b):
        if b == 0:
            return "Divisor is Zero"

        if a == 0:
            return 0

        if a > 0 and b > 0:
            for i in range(a + 1):
                result = Calculator.multiply(self, i, b)
                if result == a:
                    return i

        elif a < 0 and b > 0:
            for i in range(abs(a) + 1):
                result = Calculator.multiply(self, -i, b)
                if result == a:
                    return -i

        elif a > 0 and b < 0:
            for i in range(a + 1):
                result = Calculator.multiply(self, -i, b)
                if result == a:
                    return -i

        elif a < 0 and b < 0:
            for i in range(abs(a) + 1):
                result = Calculator.multiply(self, i, b)
                if result == a:
                    return i

        return None
    # wrong code
    # def modulo(self, a, b):
    #     while a <= b:
    #         a = a-b
    #     return a

    def modulo(self, a, b):
        if b == 0:
            return "Divisor is Zero"
        
        if a >= 0:
            while a >= abs(b):
                a -= abs(b)
            return a
        else:
            while a <= -abs(b):
                a += abs(b)
            return a

# Example usage:
if __name__ == "__main__":
    calc = Calculator()
    print("This is a simple calculator class!")
    print("Example: addition: ", calc.add(1, 2))
    print("Example: subtraction: ", calc.subtract(4, 2))
    print("Example: multiplication: ", calc.multiply(2, 3))
    print("Example: division: ", calc.divide(10, 2))
    print("Example: modulo: ", calc.modulo(10, 3))
