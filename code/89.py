a, r, n = map(int, input().split())
count = 1
while True:
    if count == n:
        break
    else:
        a *= r
        count += 1
print(a)