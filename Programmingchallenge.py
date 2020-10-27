rows = int(input("Enter number of rows: "))
columns = int(input("Enter number of columns: "))
matrix = []
repetition = int(input("Enter the repetition count: "))
flat=[]
prev = -1
count = 0
flag = 0
out = []
for i in range(rows):
    inp_matrix = []
    for j in range(columns):
        inp_matrix.append(int(input()))
    matrix.append(inp_matrix)
print("The given matrix is as follows...")
for i in range(rows):
    for j in range(columns):
        print(matrix[i][j], end=' ')
    print()
for sublist in matrix:
    for item in sublist:
        flat.append(item)
#print(flat)
# for e in flat:
#     if([e]*repetition):
#         print(int(flat[e]))

# out = flat.count(repetition)
# print(out)

flat.sort()
for item in flat:
    if item == prev:
        count = count + 1
    else:
        count = 1
    prev = item

    if count == repetition:
        flag = 1
        out.append(item)
        print("The number(s) which repeated for {0} times is {1}".format(repetition,out))
if flag == 0:
    print("No occurrences found")

