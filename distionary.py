"""dist={1:"rama",2:"sita",3:"krishna",4:"radha",5:"akrura",6:"balaram"}
print("distionary",dist)
dist1=dist.copy()#copys dist to dist1
print("copy(dist1)",dist1)

dist.clear()   # total distionary deleted
print("after using clear()",dist)

print("key of 1st element:",dist1.get(1))# get function

print("key elements:",dist1.keys())# keys function displays all keys
print("values in distonary",dist1.values())#like keys() it displays all values

print("after using pop(5) ",dist1.pop(5),dist1)# using pop() you can delete selected item
print("after using popitem()",dist1.popitem(),dist1)# using popitem() you delete last most key and value

dist1.update({5:"balaram"})#using update you can update the distonary
print("after using update()",dist1)
"""
#creating empty distionary
dist={}
print(dist)
#adding elements to the dist




