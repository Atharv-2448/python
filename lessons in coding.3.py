Fruits= ["Apple","Mango","guava"]
print(Fruits)

Vegitables= ["Tomato","Potato","Lettice"]
print(len(Vegitables))

list1= ["Cup","Plate","Utensils"]
list2= [3,4,7]
list3= [True,False]
print(list1)
print(list2)
print(list3)

list4= ["ABCD",48,False,"Game"]
print(list4)

Alist= ["Table","Chair","Rug"]
print(type(Alist))

Blist= list(("Lamp","Sofa","Time"))
print(Blist)

Clist= ["Clip","Pin","Hook"]
print(Clist[-3])

Dlist= ["Bag","Drawer","Cupbourd"]
print(Dlist[2:-3])

Elist= ["Towel","Soap","Water"]
print(Elist[:-1])

Flist= ["Bottle","Glass","Jug"]
print(Flist[-3:])

Thislist= ["Calender","Planner","Notepad"]

if "Notepad" in Thislist:
    print("Yes, Notepad is in this list")

Glist= ["Ruler","Sharpener","Eraser"]
Glist.append("Stapler")
print(Glist)

Hlist= ["Pencil","Pen","Marker"]
Hlist.insert(2,"Highlighter")
print(Hlist)

Ilist= ["Candle","Light-Bulb","Lantern"]
list5= ["Tube-Light","Light-Pendent","Chandelier"]
Ilist.extend(list5)
print(Ilist)

Jlist= ["Duster","Chalk","Refill"]
list6= ("Staples","Punching-Machine")
Jlist.extend(list6)
print(Jlist)

Klist= ["Mask","Safety-Glasses","Safety-Visor"]
Klist.remove("Mask")
print(Klist)

L_ist= ["White-Board","Black-board","Pin-board"]
L_ist.pop(2)
print(L_ist)

Mlist= ["Bowl","Can","Jar"]
Mlist.pop()
print(Mlist)

Nlist= ["Screen","Key-board","Mouse"]
del Nlist[2]
print(Nlist)
