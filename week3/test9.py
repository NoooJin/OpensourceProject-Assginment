# i = 0
# while i < 3 :
#     print("%d : 안녕하세요? while 문을 공부중입니다. ^^" % i)
#     i = i + 1
# print("-----------------------------------------------")
# i, hap = 0, 0

# i = 1
# while i < 11:
#     hap = hap + i
#     i = i + 1

# print("1에서 1 0까지의 합계: %d" % hap)
# print("-----------------------------------------------")
# ## Code06-10.py
# hap = 0
# a, b = 0, 0

# while True:
#     a = int(input("더할 첫 번째 수를 입려하세요: "))
#     b = int(input("더할 두 번째 수를 입려하세요: "))
#     hap = a + b
#     print("%d + %d = %d" % (a, b, hap))
# print("-----------------------------------------------")
## Code06-11.py
ch = ""
a, b= 0, 0

while True:
    a = int(input("첫 번째 수를 입려하세요: "))
    b = int(input("두 번째 수를 입려하세요: "))
    ch = input("계산할 연산자를 입력하세요: ")

    if(ch == "+"):
        print("%d + %d = %d" % (a, b, a + b))
    elif(ch == "-"):
        print("%d - %d = %d" % (a, b, a - b))
    elif(ch == "*"):
        print("%d * %d = %d" % (a, b, a * b))
    elif(ch == "/"):
        print("%d / %d = %d" % (a, b, a / b))
    elif(ch == "%"):
        print("%d % %d = %d" % (a, b, a % b))
    elif(ch == "//"):
        print("%d // %d = %d" % (a, b, a // b))
    elif(ch == "**"):
        print("%d ** %d = %d" % (a, b, a ** b))
    else:
        print("연산자를 잘못 입력했습니다.")