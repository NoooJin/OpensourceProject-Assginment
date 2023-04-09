# # 중첩 for문

# for i in range(0, 3, 1):
#     for k in range(0, 2, 1):
#         print("파이썬은 꿀잼입니다. ^^(i값 : %d, k값 %d)"%(i, k))

# # Code06-07.py

# for i in range(2, 10, 1):
#     for k in range(1, 10, 1):
#         print("%d X %d = %2d" % (i, k, i * k))
#     print("")

# Code06-08.py
## 전역 변수 선언 부분 ##
i, k, guguLine = 0, 0, ''

## 메인 코드 부분 ##
for i in range(2, 10):
    guguLine = guguLine + ("#  %d 단 #" % i)

print(guguLine)

for i in range(1, 10):
    guguLine = ""
    for k in range(2, 10):
        guguLine = guguLine + str("%2dX %2d=%2d" % (k, i, k*i))
    print(guguLine)