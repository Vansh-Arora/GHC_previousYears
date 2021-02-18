inputFile = open("F:\\GHC_previousYears\\b_lovely_landscapes.txt","r")
lines = inputFile.readline()
dic1 = {}
dic2 = {}
for i in range(3):
    myList = (inputFile.readline()).split()
    dic1[i] = myList[1]
    dic2[i] = myList[1:]
print(dic1)
print(dic2)