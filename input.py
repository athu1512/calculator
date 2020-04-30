import calculator as c

a=int(input("Enter the first number"))
b=int(input("Enter the second number "))
ch=0
while ch!=6:
    print("MENU")
    print("1.ADD \n 2.SUBTRACT\n 3.MULTIPLICATON \n 4.DIVISION \n 5.MODULUS \n 6.EXIT")
    ch=int(input("enter your choice"))
    if (ch==1):
        z=c.add(a,b)
        print(z)
    elif(ch==2):
        z=c.sub(a,b)
        print(z)
    elif(ch==3):
        z=c.mult(a,b)
        print(z)
    elif(ch==4):
        z=c.div(a,b)
        print(z)
    elif(ch==5):
        z=c.mod(a,b)
        print(z)
    elif(ch==6):
        print("exit")
    else:
        print("Invalid Number")