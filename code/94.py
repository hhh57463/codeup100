n = int(input())
a = map(int, input().split())
a = list(a)
min = a[0]
for i in range(1, n):
    if min > a[i]:
        min = a[i]
print(min)