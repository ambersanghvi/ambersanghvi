c= input(""" Enter your choice: 'R' or 'P' or 'S' """)
import random
d = ['R','P', 'S']
n = random.choice(d)
print("Computer's Choice: ",n)
if n==c:
    print("A Draw")
elif n =='R':
    if c=='P':
        print("You Win")
    else:
        print("You Loss")
elif n=='P':
    if c=='R':
        print("You Loss")
    else:
        print("You Win")
elif n=="S":
    if c=="R":
        print("You Win")
    else:
        print("You Loss")
