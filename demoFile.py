# DemoFile.py

#쓰기

f = open("c:\\work\\text.txt","wt",encoding="utf-8")
f.write("첫번째라인\n두번째라인\n세번째라인\n")

f.close()

#읽기

f= open(r"c:\work\text.txt","rt",encoding="utf-8")
result = f.read()


#print(result)
print(result)
f.close()



