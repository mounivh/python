
print(".......................welcome to krishna's super market..............................")
name=input("enter your name ::")
print("HELLO ",name," ,WELCOME TO KRISHNA'S SUPER MARKET")
print("our products are::")


our_products="""
                 ITEM            QUANTITY  PRICE
            ........................................    
                1:milk           500ml    30rs
                2:curd           500ml    30rs
                3:juce           1lt      50rs
                4:soap           1pack    50rs
                5:toothbrush     1pack    40rs
                6:paste          100g     40rs
                7:water bottle   1lt      20rs
                8:boost          500g     120rs
                9:maggi          1pack    50rs"""
print("*********************our products are:*************************************")
print(our_products)


selected_item=[]
item_price=[]
item_quantity=[]
total_items=[]
price1=[]
total_price=0


products={'milk':30,'curd':30,'juce':50,'soap':50,'toothbrush':40,'paste':40,'waterbottle':20,'boost':120,'maggi':50}

select=input("if u want to buy the items ???\n please press 'y' for shopping|'n' for no:: ")
if select=="y":
    for i in range(len(products)): 
        item=input("select ur items :: if you r done  n ::")# selected item stored in item
        if item=="n":
            break
        else:
            quantity=int(input("enter the quantity:"))#selected quantity stored in quantity
            for s in products.keys():#check the keys in dictionary of product
                if item==s:# if ur selected item and produduct key is same
                    selected_item.append(item)#adding selected item in slected_item[] list
                    k=products.get(item)#by using get() u can get the price of items in product{}
                    item_price.append(k)#adding price in item_price[] list
                    item_quantity.append(quantity)#adding quantity in item_quanty[] list
                    price=quantity*k#total price of each item
                    price1.append(price)#adding total price of each item into price1[] list
                   
else:
    print("THANK YOU FOR VISITING KRISHNA'S SUPER MARKET")


print("***"*30)
print("items","\t"*3,"quantity","\t"*3,"price","\t"*3,"total")
print("***"*30)

for i in range(len(selected_item)):
     print(selected_item[i],"\t"*4,item_quantity[i],"\t "*3,item_price[i],"\t "*3,price1[i])

            
print("....................................................................................................") 
for i in range(len(price1)):#for getting total of all items
    total_price+=price1[i]
    
gst=(total_price*5)/100 # for gst
bill=total_price+gst
    
    
print("TOTAL COST OF ITEMS ","\t"*8,total_price) # for display 
print("GST","\t"*10,gst)
print("TOTAL AMOUNT IS ","\t"*8,bill)

print("."*40,"thanks for shopping ","."*40)
print("."*40,"**PLEASE VISIT AGAIN**","."*40)
        
            
            
        
        
            

    
