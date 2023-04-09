# # 뮤터블 시퀀스 원소를 연순으로 정렬

# from typing import Any, MutableSequence

# def reverse_array(a: MutableSequence) -> None:
#     """뮤터블 시퀀스 a의 원소를 역순으로 정렬"""
#     n = len(a)
#     for i in range(n // 2):
#         a[i], a[n - i - 1] = a[n - i - 1], a[i]

# if __name__ == '__main__':
#     print('배열의 원소를 역순으로 정렬합니다.')
#     nx = int(input('원소 수를 입력하세요: '))
#     x = [None] * nx

#     for i in range(nx):
#         x[i] = int(input(f'x[{i}]값을 입력하세요: '))

#     reverse_array(x)

#     print('배열 원소를 역순으로 정렬했습니다.')
#     for i in range(nx):
#         print(f'x[{i}] = {x[i]}')

# 10진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기

# def card_conv(x: int, r: int) -> str:
#     """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

#     d = ''
#     dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'

#     while x > 0:
#         d += dchar[x % r]
#         x //= r

#     return d[::-1]

# if __name__ == '__main__':
#     print("10진수를 n진수로 변환합니다.")

#     while True:
#         while True:
#             no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요: '))
#             if no > 0:
#                 break
        
#         while True: # 2~36진수와 정숫값을 입력받음
#             cd = int(input('어떤 진수로 변환할까요?: '))
#             if 2 <= cd <= 36:
#                 break
        
#         print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

#         retry = input("한 번 더 변환할까요?(Y -> 예 / N -> 아니요): ")
#         if retry in {'N', 'n'}:
#             break

# 10 진수 정숫값을 입력받아 2~36진수로 변환하여 출력하기

# def card_conv(x: int, r: int) -> str:
#     """정숫값 x를 r진수로 변환한 뒤 그 수를 나타내는 문자열을 반환"""

#     d = ''
#     dchar = '0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ'
#     n = len(str(x))

#     print(f'{r:2} | {x:{n}d}')

#     while x > 0:
#         print('  +' + (n + 2) * '-')
#         if x // r:
#             print(f'{r:2} | {x // r:{n}d} --- {x % r}')
#         else:
#             print(f'     {x // r:{n}d} --- {x % r}')
#         d += dchar[x % r]
#         x //= r

#     return d[::-1]

# if __name__ == '__main__':
#     print("10진수를 n진수로 변환합니다.")

#     while True:
#         while True:
#             no = int(input('변환할 값으로 음이 아닌 정수를 입력하세요: '))
#             if no > 0:
#                 break
        
#         while True: # 2~36진수와 정숫값을 입력받음
#             cd = int(input('어떤 진수로 변환할까요?: '))
#             if 2 <= cd <= 36:
#                 break
        
#         print(f'{cd}진수로는 {card_conv(no, cd)}입니다.')

#         retry = input("한 번 더 변환할까요?(Y -> 예 / N -> 아니요): ")
#         if retry in {'N', 'n'}:
#             break

# # 1,000 이하의 소수를 나열하기

# counter = 0

# for n in range(2, 1001):
#     for i in range(2, n):
#         counter += 1
#         if n % i == 0:
#             break
    
#     else:
#         print(n)

# print(f'나눗셈을 실행한 횟수: {counter}')

# # 1,000 이하의 소수를 나열하기(알고리즘 개선 1)

# counter = 0
# ptr = 0
# prime = [None] * 500

# prime[ptr] = 2
# ptr += 1

# for n in range(3, 1001, 2):
#     for i in range(1, ptr):
#         counter += 1
#         if n % prime[i] == 0:
#             break
    
#     else:
#         prime[ptr] = n
#         ptr += 1
    
# for i in range(ptr):
#     print(prime[i])

# print(f'나눗셈을 실행한 횟수: {counter}')

# 1,000 이하의 소수를 나열하기(알고리즘 개선 2)

counter = 0
ptr = 0
prime = [None] * 500

prime[ptr] = 2
ptr += 1

prime[ptr] = 3
ptr += 1

for n in range(5, 1001, 2):
    i = 1
    while prime[i] * prime[i] <= n:
        counter += 2
        if n % prime[i] == 0:
            break
        i += 1
    else:
        prime[ptr] = n
        ptr += 1
        counter += 1

for i in range(ptr):
    print(prime[i])
print(f'곰셈과 나눗셈을 실행한 횟수: {counter}')