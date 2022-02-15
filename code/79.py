n = int(input())
count = 1
sum = 0
while True:
    if sum > n:
        break
    sum += count
    if sum < n:
        count += 1
print(count)