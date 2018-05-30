if __name__ == '__main__':
    n = int(input())

# print(bin(n).count("1"))                          #for counting number of 1s

print(max(map(len, bin(n)[2:].split('0'))))

# explanation

# convert integer to binary representation bin(n)
# strips 0b from the binary representation bin(n)[2:]
# split the string on character 0 bin(n)[2:].split('0')
# find the string that has the maximum length and return the number
