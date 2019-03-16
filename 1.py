num = int(input())


# 1
total_array = []
for i in range(num):
    array = []
    for j in range(i+1):
        array.append(1)
    total_array.append(array)

for i in range(len(total_array)-1):
    for j in range(len(total_array[i])):
        if j == 0:
            continue
        total_array[i+1][j] = total_array[i][j] + total_array[i][j-1]

# 2
total_array = [[1] * (i+1) for i in range(num)]
for i in range(len(total_array)-1):
    for j in range(1, len(total_array[i])):
        total_array[i+1][j] = total_array[i][j] + total_array[i][j-1]

print(total_array)

