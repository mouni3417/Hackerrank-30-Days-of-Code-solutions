n = int(input())
dictOfEntries  ={}                                   #empty dictionary
for i in range(0,n):
    userInput = input().split()
    dictOfEntries[(userInput[0])] = userInput[1]    # name as key , number as value

while True:
    query = input()
    if query != "":

        if query in dictOfEntries.keys():
            print(query + "=" + str(dictOfEntries[query]))
        else:
            print("Not found")
    else:
        break
