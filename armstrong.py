a = int(input("Enter a number: "))
c = 0
d = a
while a>0:
    c= c+pow(a%10,3)
    a//=10
if c==d:
    print("Is a armstrong number.")
else:
    print("Not")
