# 딕셔너리의 생성
print("<딕셔너리의 생성>")
dic1 = {'1': 'a', '2': 'b', '3': 'c'}
print(dic1)

dic2 = {'a': '1', 'b': '2', 'c': '3'}
print(dic2)

# 딕셔너리에 정보 추가
print("<딕셔너리에 정보 추가>")
student1 = {'학번' : 1000, '이름': '홍길동', '학과': '컴퓨터학과'}
print(student1)

student1['연락처'] = '010-1111-2222'
print(student1)

student1['학과'] = '파이썬학과'
print(student1)

student1 = {'학번': 1000, '이름': '홍길동', '학과': '파이썬학과', '학번': 2000}

# 딕셔너리의 사용
print("<딕셔너리의 사용>")
print(student1['학번'])
print(student1['이름'])
print(student1['학과'])

print(student1.get('이름'))

# print(student1['주소']) 에러 코드
print(student1.get('주소')) # 에러 안남

print(student1.keys())

print(list(student1.keys()))

print(student1.values())

print(student1.items())

print('이름' in student1)