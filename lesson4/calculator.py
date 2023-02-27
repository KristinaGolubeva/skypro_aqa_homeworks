class Calculator: 

    def sum(self, a,b):
        result = a+b
        return result

    def sub(self,a,b):
        result = a-b
        return result

    def mul(self,a,b):
        return a*b

    def div(self,a,b):
        if (b==0):
            raise ArithmeticError("На ноль делить нельзя")

        return a/b

    def pow(self,a,b=2):   #когда одна переменная чему-то равна, пользователь может ввести вместо нее другое число и оно заменится, или не вводить ничего и по умолчанию будет внесенное нами значение
        return a**b


    def avg(self,nums):
        if (len(nums) == 0):
            return 0

        s=0
        for num in nums:
            s = s + num

        l = len(nums)
        return self.div(s,l)

    
    