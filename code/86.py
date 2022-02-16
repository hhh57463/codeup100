a = int(input())
b = 1
sum = 0
while True:
    sum += b
    if sum >= a:
        break
    else:
        b += 1
print(sum)