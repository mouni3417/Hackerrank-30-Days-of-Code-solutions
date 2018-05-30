if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    data = list(reversed(arr))
    print(*data, sep=' ')        #* opens a list. Gives the value. if lis is is a list, lis = [*lis]