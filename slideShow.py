inputFile = open("F:\\GHC_previousYears\\b_lovely_landscapes.txt","r")
outputFile = open("F:\\GHC_previousYears\\sol.txt","w")
outputFile2 = open("F:\\GHC_previousYears\\sol2.txt","w")

lines = int(inputFile.readline())
dic1 = {}
dic2 = {}
for i in range(lines):
    myList = (inputFile.readline()).split()
    dic1[i] = int(myList[1])
    dic2[i] = myList[2:]
for i in range(lines):
    outputFile.write(str(dic1[i]) + " " + str(i) + "\n")
    outputFile2.write(str(dic2[i]) + "\n") 
