ss = 'Pythjon is Easy. 그래서 programing이 재미있습니다.'
print(ss.upper())
print(ss.lower())
print(ss.swapcase())
print(ss.title())

ss = '파이썬 공부는 즐겁습니다. 물론 모든 공부가ㅏ 다 재미있지는 않죠.^^'
print(ss.count('공부'))
print(ss.find('공부'), ss.rfind('공부'), ss.find('공부', 5), ss.find('없다'))
print(ss.index('공부'), ss.rindex('공부'), ss.index('공부', 5))
print(ss.startswith('파이썬'), ss.startswith('파이썬', 10), ss.startswith('^^'))

ss = ' 파 이 썬 '
print(ss.strip())
print(ss.rstrip())
print(ss.strip())

ss = '----파---이---썬----'
print(ss.strip('-'))
ss = '<<<파 << 이 >> 썬>>>'
print(ss.strip('<>'))

ss = '열심히 파이썬 공부 중~~'
print(ss.replace('파이썬', 'Python'))

ss = 'Python을 열심히 공부 중'
print(ss.split())
ss = '하나:둘:셋'
print(ss.split(':'))
ss = '하나\n\둘\n셋'
print(ss.splitlines())
ss = '%'
print(ss.join('파이썬'))

before = ['2019', '12', '31']
after = list(map(int, before))
print(after)

ss = '파이썬'
print(ss.center(10))
print(ss.center(10, '-'))
print(ss.ljust(10))
print(ss.zfill(10))

print('1234'.isdigit())
print('abcd'.isalpha())
print("abc123".isalnum())
print('bcd'.islower())
print("ABCD".isupper())
print('   '.isspace())