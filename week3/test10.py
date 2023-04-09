# for i in range(1, 100):
#     print("for 문을 %d번 실행했습니다." % i)
#     break

# hpa = 0
# a, b = 0, 0

# while True:
#     a = int(input("더할 첫 번째 수를 입력하세요: "))
#     if a == 0:
#         break
#     b = int(input("더할 두 번째 수를 입력하세요: "))
#     hap = a + b
#     print("%d + %d = %d" % (a, b, hap))

# print("0을 입력해 반복문을 탈출했습니다.")

# hpa, i = 0, 0

# for i in range(1, 101):
#     hap += i

#     if hap >= 1000:
#         break
# print("1~100의 합계를 최초로 1000이 넘게 하는 숫자: %d" % i)

# Code06-14.py
hap, i = 0, 0

for i in range(1, 101):
    if i % 3 == 0:
        continue

    hap += i

print("1~100의 합계(3의 배수 제외) : %d" % hap)