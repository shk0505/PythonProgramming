inFp = None
inList = ""

inFp = open("C:\\Users\\hongk\\Desktop\\PythonProgramming\\10주차\\FileTest\\data1.txt", "r", encoding="UTF8")

inList = inFp.readlines()
#print(inList)
for i, inStr in enumerate(inList) :
    print(i+1,'\b:', inStr, end = "")

inFp.close()