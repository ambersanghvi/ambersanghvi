a = []
for i in range(11):
    d = int(input("Enter a number:"))
    if d%2==0:
        a.append(d)
print("The list is: ", *a)
