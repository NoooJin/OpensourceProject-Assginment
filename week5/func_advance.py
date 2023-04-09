def outFunc(v1, v2):
    def inFunc(num1, num2):
        return num1 + num2
    return inFunc(v1, v2)

def factorial(num):
    if num <=1 :
        return num
    else :
        return num * factorial(num - 1)

print(outFunc(10, 20))

hap2 = lambda num1, num2: num1 + num2
print(hap2(10, 20))

print(factorial(4))