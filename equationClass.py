class Equation:
    def __init__(self, coef, exp):
        self.exp = exp
        self.coef = coef


    def getexponent(self):
        return self.exp


    def diff(self):
        if(self.coef == 0):
            return "0"
        elif(self.coef == 1):
            c = 1
        elif(self.coef == -1):
            c = -1
        else:
            c = self.coef


        e = self.exp - 1
        if(e == 0):
            return "1"

        return "{}x^{}".format(c*self.exp, e)


    def __str__(self):
        cof = self.coef
        if(self.coef == 1):
            cof = ""
        elif(self.coef == -1):
            cof = "-"
        return "{}x^{}".format(cof, self.exp)



eq1 = Equation(1, 5)
eq2 = Equation(25, 4)

print(eq1)
print(eq1.diff())
print(eq2)
print(eq2.diff())
