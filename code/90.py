a, m, d, n = map(int, input().split())
count = 1
while True:
    if count == n:
        break
    else:
        a = a * m + d
        count += 1
print(a)