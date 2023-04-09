# # 5-1 if 문의 형식과 순서도

# # if 문이 참일 때
# a = 99
# if a < 100:
#     print("100보다 작군요.")

# # if 문이 거짓일 때, 두 문장을 if 문 안에 넣을 때
# a = 200

# if a < 100:
#     print("100보다 작군요.")
# print("거짓이므로 이 문장은 안 보이겠죠?")

# print("프로그램 끝")

# a = 200

# print("--------------------------------")

# if a < 100:
#     print("100보다 작군요.")
#     print("거짓이므로 이 문장은 안 보이겠죠?")

# print("프로그램 끝")

# # 기본 if 문
# a = 200

# if a < 100:
#     print("100보다 작군요.")
# else:
#     print("100보다 크군요.")

# print("-------------------")
# # 기본 if 문 2
# a = 200

# if a < 100:
#     print("100보다 작군요.")
#     print("참이면 이 문장도 보이겠죠?")
# else:
#     print("100보다 크군요.")
#     print("거짓이면 이 문장도 보이겠죠?")

# print("프로그램 끝")

# # code 05-05.py
# a = int(input("정수를 입력하세요: "))

# if a % 2 == 0:
#     print("짝수를 입력했군요")
# else:
#     print("홀수를 입력했군요")
# print("-----------------------")

# # code 05-06.py
# a = 75

# if a > 50:
#     if a < 100:
#         print("50보다 크로 100보다 작군요.")
#     else:
#         print("와 ~~ 100보다 크군요.")
# else:
#     print("에고~~ 50보다 작군요")

# # Code 05-08
# score = int(input("점수를 입력하세요: "))

# if score >=90:
#     print("A")
# elif score >= 80:
#     print("B")
# elif score >= 70:
#     print("C")
# elif score >= 60:
#     print("D")
# else:
#     print("F")

# print("학점입니다. ^^")

# 삼항 연산자로 사용한 if 문
# 일반 if 문
jumsu = 55
res = ''
if jumsu >= 60:
    res = '합격'
else:
    res = '불합격'
print(res)

# 3항 연산자
res = '합격' if jumsu >= 60 else '불합격'
print(res)