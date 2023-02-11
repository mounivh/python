#simple interest and compound interest
'''
simple interest 
p= principle amount
t= time in years 
r= rate of interest 

si=(p*t*r)/100
ci=A-p
A=p(power(1+r/n*100,n*t)) 

'''
"""
print(" **************simple interest************ \n")
p=int(input("enter the principle amount "))
t=int(input("enter the years "))
r=float(input("enter rate of interest "))
#si= simple interest
si=(p*t*r)/100
print("simple interest of principle amount is ",p,"is",si)
print(" ***************compound interest***************** \n")
"""

















#ci= compound interest
#A=total meturity ammount
'''
if n=numberof times interest applied per year  which means n=1
if quater means n=4
if everymonth means n=12
if half year means n=2

'''
p=int(input("enter the principle amount "))
t=int(input("enter the years "))
r=float(input("enter rate of interest "))
n=int(input("if you want to add interest per year enter 1 \n  per month enter 12 \n per quater enter 4 \n per half an year enter 2  \n"))
R=r/100
A=p*((1+R/n)**(n*t))
print("meturity amount is  ",A)
ci=A-p
print("compound interest is ",ci)


