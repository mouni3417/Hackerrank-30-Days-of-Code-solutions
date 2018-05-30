n = int(input())

for i in range(0, n):
    text = str(input())
    listOfChars = list(text)
    oddList = listOfChars[1::2]   # list slicing method , list [start:stop:step]
    evenList = listOfChars[0::2]
    strOddList = ''.join(oddList)  #Converting list to string
    strEvenList = ''.join(evenList)
    print( strEvenList + " " + strOddList)