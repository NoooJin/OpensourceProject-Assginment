## 튜플 생성
print("<튜플 생성>")
tt1 = (10, 20, 30); print(tt1)
tt2 = 10, 20, 30; print(tt2)
tt3 = (10); print(tt3)
tt4 = 10; print(tt4)
tt5 = (10,); print(tt5)
tt6 = 10,; print(tt6)

tt1 = (10, 20, 30, 40)
print(tt1[0])
print(tt1[0] + tt1[1] + tt1[2])

# 튜플 범위에 접근
print("<튜플 범위에 접근>")
print("tt1[1:3]: ", tt1[1:3])
print("tt1[1:]: ", tt1[1:])
print("tt1[:3]: ", tt1[:3])

# 튜플의 덧셈 및 곱셈 연산
print("<튜플의 덧셈 및 곱셈 연산>")
tt2 = ('A', 'B')
print("tt1 + tt2", tt1 + tt2)
print("tt1 * 3", tt1 * 3)

# 튜플 > 리스트 > 튜플 변환
print("<튜플 > 리스트 > 튜플 변환>")
myTuple = (10, 20, 30)
myList = list(myTuple)
myList.append(40)
myTuple = tuple(myList)
print(myList)