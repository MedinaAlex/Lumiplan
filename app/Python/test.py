i = 0
f = True
for _ in range(10):
    print(f)
    if f:
        f = False
        continue
    print(i)
    i += 1
