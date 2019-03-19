num = int(input())


# 1
answer_array = []
for i in range(num):
    array = []
    for j in range(i+1):
        array.append(1)
    answer_array.append(array)

for i in range(len(answer_array)-1):
    for j in range(len(answer_array[i])):
        if j == 0:
            continue
        answer_array[i+1][j] = answer_array[i][j] + answer_array[i][j-1]

# 2
answer_array = [[1] * (i+1) for i in range(num)]
for i in range(len(answer_array)-1):
    for j in range(1, len(answer_array[i])):
        answer_array[i+1][j] = answer_array[i][j] + answer_array[i][j-1]

print(answer_array)

