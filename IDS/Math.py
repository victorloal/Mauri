class maths:
    def average(self,arg=[]):
        result = sum(arg)/len(arg)
        result -= result*0.05
        result = round(result, 5)
        return result
    
    