#coding=utf-8




#1 捕获所有异常
try:
    print(a)

except: #这个except是包含了所有的错误信息（可以捕获所有异常）
    print("产生了一个错误,请检查...")


#2 捕获多个异常
try:
	#print(a)
	open("a.txt")

except NameError:
   	print("产生了一个异常--01--")
except FileNotFoundError:
   	print("产生了一个异常--02--")



#3 捕获多个异常
try:
	print(a)
    #open("a.txt")
#当产生这两个异常时，在except当中解决的方法一样时。    
except (NameError,FileNotFoundError): 
    print("产生了一个异常")


#4 捕获多个异常,并且生成系统自带的异常原因
try:
    print(a)
    open("a.txt")
except (NameError,FileNotFoundError) as result:
    print("产生了一个异常...%s"%result)


#5 捕获所有异常（IndentationError错误，键盘输入错误等无法捕获），
#	并且生成系统自带的异常原因
try:
    print(a)
    open("a.txt")
except Exception as result:
    print("产生了一个异常...%s"%result)

