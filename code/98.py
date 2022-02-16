list_ant = []
x = 1
y = 1
food_count = 0
for i in range(10):
    list_ant.append([])
    for j in range(10):
        list_ant[i].append(0)

for i in range(10):
    list_ant[i] = list(map(int, input().split()))

for i in range(10):
    for j in range(10):
        if list_ant[i][j] == 2:
            food_count += 1

while True:
    if food_count > 0:
        if list_ant[y][x + 1] != 1:
            if list_ant[y][x] != 9:
                list_ant[y][x] = 9
            x += 1
            if list_ant[y][x] == 2:
                food_count -= 1
            list_ant[y][x] = 9
        elif list_ant[y + 1][x] != 1:
            if list_ant[y][x] != 9:
                list_ant[y][x] = 9
            y += 1
            if list_ant[y][x] == 2:
                food_count -= 1
            list_ant[y][x] = 9
        else:
            break
    else:
        break

for i in range(10):
    for j in range(10):
        print(list_ant[i][j],end=' ')
    print()