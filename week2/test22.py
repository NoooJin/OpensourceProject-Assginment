print(10 & 7, 123 & 456, 0xFFFF & 0x0000)
print()
print(10 | 7, 123 | 456, 0xFFFF | 0x0000)
print()
print(10 ^ 7, 123 ^ 456, 0xFFFF ^ 0x0000)
print()

a = ord('A')
mask = 0x0F

print("%x & %x = %x" % (a, mask, a&mask))
print("%x | %x = %x" % (a, mask, a|mask))

mask = ord('a') - ord('A')

b = a^mask
print("%c ^ %d = %c" % (a, mask, b))
a = b ^ mask
print("%c ^ %d = %c" % (b, mask, a))

a = 12345
print(~a + 1)

a = 10
print(a << 1, a << 2, a << 3, a << 4)

a = 10
print(a >> 1, a >> 2, a >> 3, a >> 4)

a = 100
result = 0
i = 0

for i in range(1, 5):
    result = a << i
    print("%d << %d = %d" % (a, i, result))

for i in range(1, 5):
    result = a >> i
    print("%d >> %d = %d" % (a, i, result))