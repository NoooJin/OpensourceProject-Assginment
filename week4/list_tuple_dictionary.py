print('<set 함수 사용>')
mySet1 = {1, 2, 3, 3, 3, 4}
print(mySet1)

salesList = ['삼각김밥', '바나나', '도시락', '삼각김밥', '삼각김밥', '도시락', '삼각김밥']
print(set(salesList))

# 딕셔너리 사이의 연산
print('<딕셔너리 사이의 연산>')
mySet1 = {1, 2, 3, 4, 5}
mySet2 = {4, 5, 6, 7}
print(mySet1 & mySet2)
print(mySet1 | mySet2)
print(mySet1 - mySet2)
print(mySet1 ^ mySet2)

print(mySet1.intersection(mySet2))
print(mySet1.union(mySet2))
print(mySet1.difference(mySet2))
print(mySet1.symmetric_difference(mySet2))

# 컴프리핸션
print('<컴프리핸션>')
numList = []
for num in range(1, 6):
    numList.append(num)
print(numList)

numList = [num for num in range(1, 6)]
print(numList)

numList = [num * num for num in range(1, 6)]
print(numList)

numList = [num for num in range(1, 21) if num % 3 == 0]
print(numList)

# 동시에 여러 리스트에 접근
print('<동시에 여러 리스트에 접근>')
foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sides = ['오뎅', '단무지', '김치']
for food, side in zip(foods, sides):
    print(food, '-->', side)

foods = ['떡볶이', '짜장면', '라면', '피자', '맥주', '치킨', '삼겹살']
sides = ['오뎅', '단무지', '김치']
tupList = list(zip(foods, sides))
dic = dict(zip(foods, sides))
print(tupList)
print(dic)

# 리스트의 복사 얕은 복사
print('<리스트의 복사 얕은 복사>')
oldList = ['짜장면', '탕수육', '군만두']
newList = oldList
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)

# 깊은 복사
print('<깊은 복사>')
oldList = ['짜장면', '탕수육', '군만두']
newList = oldList[:]
print(newList)
oldList[0] = '짬뽕'
oldList.append('깐풍기')
print(newList)