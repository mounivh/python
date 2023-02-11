#finding largest num in given num
a,b,c=input("enter three numbers\n").split()

if a>b and a>c:
  print("largest num is" ,a)
elif b>a and b>c:
    print("largest num is ",b)  
else:
    print("largest num is ",c)    
    