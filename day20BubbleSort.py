n = int(input().strip())
a = list(map(int, input().strip().split(' ')))
# Write Your Code Here
swaps = 0
temp =0
for i in range(0,n):
    for j in range(0,n-1):
        if(a[j]>a[j+1]):
            temp = a[j]
            a[j]= a[j+1]
            a[j+1] = temp
            swaps += 1

print("Array is sorted in " + str(swaps) + " swaps.")
print("First Element: " +  str(a[0]))
print("Last Element: " + str(a[n-1]))