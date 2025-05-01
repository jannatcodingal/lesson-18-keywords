a=int(input("Enter the amount of the object: "))
b=int(input("amount paid: "))
c=a-b
if c==0:
    print("you dont have dept")
else:
   if c!=0:
      print("dept is due. Pay: ",c)