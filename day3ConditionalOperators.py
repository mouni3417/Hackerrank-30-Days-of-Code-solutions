N = int(input())

if N % 2 != 0:
    print("Weird")
else:
    if N > 20 or N == 4:
        print("Not Weird")
    else:
        print("Weird")
