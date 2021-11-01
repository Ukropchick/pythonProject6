
a = 6
b = 7
c = 8
c = int("8")
a = list([4, 6, 7])

stats = [a, b, c]
print(stats)

del stats[2]
print(stats)
print(stats)

a = [1, 2, 3, 4, 5, 6, 7, 8, "a"]
print(a[0])
for i in range(len(a) // 2):
    a.append(i)
print(a[-1])
print(a[len(a) - 1])

print(a)
b = a[2:3]
print(b)
c = a[:3]
print(c)
d = a[2:]
print(d)


test = []
# основные функции над списками
test.append(4)
test.extend([3, 6, 0])
a = test.count(3)
test.sort()
print(test, a)

for i in test:
    print(i)
    len(test)
print(len(test))


