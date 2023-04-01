## 리스트 값에 접근하는 다양한 방법
print('리스트에 인덱스를 이용하여 접근')
aa = [10, 20, 30, 40]
print("aa[-1]은 %d, aa[-2]는 %d" % (aa[-1], aa[-2]))

print("\n리스트에 접근하는 방법 콜론")
print(aa[0:3])
print(aa[2:4])

print(aa[2:])
print(aa[:2])

print('\n인덱스에 연산을 적용하여 출력')
aa = [10, 20, 30]
bb = [40, 50, 60]
print("aa + bb = %s, aa * 3 = %s" % (aa + bb, aa * 3))

aa = [10, 20, 30, 40, 50, 60, 70]
print("aa[::2] = %s, aa[::-2] = %s, aa[::-1] = %s" % (aa[::2], aa[::-2], aa[::-1]))

print("\n리스트 값 변경, 삭제하기")
aa = [10, 20, 30]
aa[1] = 200
print(aa)

a = [10, 20, 30]
aa[1:2] = [200, 201]
print(aa)

aa = [10, 20, 30]
a[1] = [200, 201]
print(aa)

aa = [10, 20, 30]
del(aa[1])
print(aa)

aa = [10, 20, 30, 40, 50]
aa[1:4] = []
print(aa)

aa = [10, 20, 30]; aa = []; print(aa)
aa = [10, 20, 30]; aa = None; print(aa)
# aa = [10, 20, 30]; del(aa); print(aa) # 오류 발생
