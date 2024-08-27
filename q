[1mdiff --git a/function1.py b/function1.py[m
[1mindex 15b658d..824a53d 100644[m
[1m--- a/function1.py[m
[1m+++ b/function1.py[m
[36m@@ -1,20 +1,12 @@[m
[31m-# function1.py[m
[32m+[m[32m#교집합 리턴하는 함수[m[41m [m
[32m+[m[32mdef intersect(prelist, postlist):[m
[32m+[m[32m    retList = [][m
[32m+[m[32m    for x in prelist:[m
[32m+[m[32m        if x in postlist and x not in retList:[m
[32m+[m[32m            retList.append(x)[m
[32m+[m[32m    return retList[m[41m [m
 [m
[31m-#1) 함수정의[m
[31m-def setValue(newValue):[m
[31m-    #지역변수 초기화[m
[31m-    x = newValue[m
[31m-    print("지역변수:",x)[m
 [m
[31m-#2) 호출[m
[31m-retValue = setValue(5)[m
[32m+[m[32m#호출[m
[32m+[m[32mprint( intersect("HAM", "SPAM") )[m
 [m
[31m-print(retValue)[m
[31m-[m
[31m-# 함수정의[m
[31m-[m
[31m-def swap(x,y):[m
[31m-    return y,x[m
[31m-[m
[31m-retValue=swap(3,7)[m
[31m-print(retValue)[m
\ No newline at end of file[m
