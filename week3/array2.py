# # 배열 원소의 최댓값 구해서 출력하기(원솟값을 입력받음)

# from array1 import max_of

# print('배열의 최댓값을 구합니다.')
# print('주의: "End"를 입력하면 종료합니다.')

# number = 0
# x= []

# while True:
#     s = input(f'x[{number}]값을 입력하세요: ')
#     if s == "End":
#         break
#     x.append(int(s))
#     number += 1

# print(f'{number}개를 입력했습니다.')
# print(f'최댓값은 {max_of(x)}입니다.')

# # 배열 원소의 최댓값을 구해서 출력하기(원솟값을 난수로 생성)

# import random
# from array1 import max_of

# print('난수의 최댓값을 구합니다.')
# num = int(input('난수의 개수를 입력하세요: '))
# lo = int(input('난수의 최솟값을 입력하세요: '))
# hi = int(input('난수의 최댓값을 입력하세요: '))
# x = [None] * num

# for i in range(num):
#     x[i] = random.randint(lo, hi)

# print(f'{(x)}')
# print(f'이 가운데 최댓값은 {max_of(x)}입니다.')

# #각 배열 원소의 최댓값을 구해서 출력하기(튜플, 문자열, 문자열 리스트)

# from array1 import max_of

# t = (4, 7, 5.6, 2, 3.14, 1)
# s = 'string'
# a = ['DTS', 'AAC', 'FLAC']

# print(f'{t}의 최댓값은 {max_of(t)}입니다.')
# print(f'{s}의 최댓값은 {max_of(s)}입니다.')
# print(f'{a}의 최댓값은 {max_of(a)}입니다.')
