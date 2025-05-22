inFp = None
inStr = ""
i = 0
j = '\b:'

inFp = open("C:\\Users\\hongk\\Desktop\\PythonProgramming\\10주차\\FileTest\\data1.txt", "r", encoding="utf8")

while True :
    inStr = inFp.readline()
    if inStr == "" :
        break;
    i += 1
    print(("%d %s" % (i, j)), inStr, end= "")

inFp.close()