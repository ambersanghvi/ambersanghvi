def cal(a , b, c):
    if c=="+":
        print("Addition=",a+b)
    elif c=="-":
        print("Subtraction=",a-b)
    elif c=="/":
        print("Division=",a/b)
    else:
        print("Multiplication=",a*b)

a, b  = map(int,input("Enter two numbers: " ).split())
c = input("Enter Operation: " )
cal(a,b,c)
