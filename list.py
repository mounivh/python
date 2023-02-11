#.............positive index.............
"""

l1=["ram","sita",1,1.2]
print(type(l1))#prints type of l1 variable
print(l1[0])#prints 0 index variable "ram" 
print(l1[0:])#prints total list from [0] to [n-1]
print(l1[:])#prints total list
print(l1[0:2])#prints l1[0],l1[1]
print(l1[1:3])#prints l1[1],l1[2]
print(l1[:3])#prints l1[0],l1[2]
print(l1[0:4:2])#list[start:stop:skip] 0:4:2 means starts from index 0 and ends at 3 skips every 2nd value then 
#o/p is ram,1 ;;sita and 1.2 were skipped
"""

"""
#...........negitive index ..................
l2=["ram",1,"sita",2]
print(l2[:-1])#prints ram,1,sita bcz starts counting index from right hand side
print(l2[-4:])# prints total list
print(l2[-4::2])#skips every 2nd value o/p is ram,sita
print(l2[-4:-1])#prints l2[-4] to l2[-2]o/p is ram,1,sita


"""
"""
#..............updating list values...........
l3=["ram","sita",1,2,3]
print(l3)
l3[2]="lakshman" #update value of  1 with lakshman so need to add index of 2 because index starts with 0
print(l3)
l3[1:3]=["sita1","lakshman1"]# to update multiple eliments like this
print(l3)
l3[-1]="hanuman"
print(l3)
"""

"""

#..............iterating of list............
l4=["ram","sita","lakshman","hanuman"]
for i in l4:
    print(i)

"""

"""

#.................append.........
l5=[]
n=int(input("how many values u r going to enter for a list"))
for i in range(0,n):
    l5.append(input("enter the element"))
print("your list is")
for i in l5:
    print(i,end=',')
print()


"""
"""

#fibnocci 
k=0
n=int(input("enter n value"))
for i in range(0,n):
    for j in range(i):
        k+=1
        print(i,end='')
    print()
"""

"""
#program using list comprehension to the cube of listed elements
print([i**3 for i in [1,2,3,4,5,6,7,8,9,10]])
"""














