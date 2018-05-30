if __name__ == '__main__':
    arr = []

for _ in range(6):
    arr.append(list(map(int, input().rstrip().split())))
temp = -500
sum = 0
x = 0
y = 1
z = 2

for i in range(4):


    a = x
    b = y
    c = z
    for j in range(4):


        sum = arr[x][j] + arr[x][j+1] + arr[x][j+2] + arr[y][j+1] + arr[z][j] + arr[z][j+1] + arr[z][j+2]
        if sum > temp:
            temp = sum
        a += 1
        b += 1
        c += 1
        sum =0
    x += 1
    y += 1
    z += 1
print(temp)