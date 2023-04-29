
from typing import MutableSequence

def insertion_sort(a: MutableSequence) -> None:
    n = len(a)
    count = 0
    for i in range(1, n):
        j = i
        tmp = a[i]
        while j > 0 and a[j - 1] > tmp:
            count += 1
            a[j] = a[j - 1]
            j -= 1
        a[j] = tmp

    print('비교를 %d번 했습니다.' % count)

if __name__ == '__main__':
    print('단순 삽입 정렬을 수행합니다.')
    num = int(input('원소 수를 입력하세요.: '))
    x = [None] * num

    for i in range(num):
        x[i] = int(input(f'x[{i}]: '))

    insertion_sort(x)

    print('오름차순으로 정렬했습니다.')
    for i in range(num):
        print(f'x[{i}] = {x[i]}')