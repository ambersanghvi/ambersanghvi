a = True
l = []
i = 10
while a:
    i = int(input("Enter a number: "))
    if i==0:
        a = False
    elif i%2==0:
        l.append(i)
print("The the list is: ", l )
    
