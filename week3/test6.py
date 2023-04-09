# # 반복문의 기초
# print("안녕하세요? for 문을 공부 중입니다. ^^")
# print("안녕하세요? for 문을 공부 중입니다. ^^")
# print("안녕하세요? for 문을 공부 중입니다. ^^")
# print('---------------------------------')

# for i in range(0, 3, 1):
#     print("안녕하세요? for 문을 공부 중입니다. ^^")
# print('---------------------------------')

# for i in range(2, -1, -1):
#     print("%d: 안녕하세요? for 문을 공부 중입니다. ^^"%i)
# print('---------------------------------')

# for i in range(1, 6, 1):
#     print("%d"% i, end=' ')
# print('\n---------------------------------')

# # 합계 구하기
# hap = 1 + 2 + 3 + 4 + 5 + 6 + 7 + 8 + 9 + 10
# print('1에서 10까지의 합계 : %d'%hap)
# print('---------------------------------')

# i, hap = 0, 0

# for i in range(1, 11):
#     hap = hap + i

# print('1에서 10까지의 합계 : %d'%hap)
# print('---------------------------------')

# # 500과 1000 사이에 있는 홀수의 합계
# i, hap = 0, 0

# for i in range(501, 1001, 2):
#     hap = hap + i

# print('500과 1000사이에 있는 홀수의 합계 : %d'%hap)
# print('---------------------------------')

# # 키보드로 입력한 값까지의 합계 구하기
# i, hap = 0, 0
# num = 0

# num = int(input('값을 입력하세요: '))

# for i in range(1, num + 1, 1):
#     hap = hap + i

# print("1에서 %d까지의 합계: %d"%(num, hap))
# print('---------------------------------')
# # Code06-05.py
# i, hap = 0, 0
# num1, num2, num3 = 0, 0, 0

# num1 = int(input('시작값을 입력하세요: '))
# num2 = int(input('끝값을 입력하세요: '))
# num3 = int(input('증가값을 입력하세요: '))

# for i in range(num1, num2 + 1, num3):
#     hap = hap + i

# print("%d에서 %d까지 %d씩 증가시킨 값의 합계: %d" % (num1, num2, num3, hap))
# print('---------------------------------')
# Code06-06.py

dan = int(input("단을 입력하세요: "))

for i in range(1, 10, 1):
    print("%d X %d = %2d" % (dan, i, dan * i))


