# self study 6-2

dan = int(input("단을 입력하세요: "))

for i in range(9, 0, -1):
    print("%d X %d = %2d" % (i, dan, dan * i))

# slef study 6-3

i, k = 0, 0

for i in range(2, 10, 1):
    print("##  %d단  ##" % (i))
    for k in range(1, 10, 1):
        print("%d X %d = %2d" % (i, k, i * k))