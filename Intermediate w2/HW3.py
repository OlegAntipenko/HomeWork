def fbndef(max):
    a = 0
    b = 1
    coun = 0
    while coun < max:
        yield a
        a, b = b, a + b
        coun += 1

for i in fbndef(9):
    print(i)


def come(max):
    a = 0
    b = 1
    coun = 0
    li = []
    while coun < max:
        li.append(a)
        a, b = b, a + b
        coun += 1
    return li
print(come(3))
