# Alondra H., Sadie HS. -List Project pt 2
#1/10/24
shopList = []
def removeAll():
    shopList.clear()
def sorts():
    shopList.sort()
def count():
    print(len(shopList))
print(" Welcome to grocery list app. You can jot down any products you need to buy!")
def view():
    print (shopList)
def addItem():
    add= input("What do vou want to add to the list?: ")
    shopList.append(add)
    print(shopList)
def markItem():
    ans2= (input("What would you like to mark off your list? State number on list starting from 0. "))
    shopList.remove(ans2)

#5. Remove all tasks from the list
#6. Sort the list alphabetically
#7. Count the # of Items on the To-do List

def menu():
    ans = input("What would you like to do today? [Add] items to list, [View] current list, [Mark] a completed task, or [Exit] program?, [Remove] all items off list,[Alphabetize] or [Count] items on list?: ")
    if ans == "add" or "Add":
       addItem()
    if ans == "View" or "view":
         view()
    if ans == "Mark" or "mark":
        markItem()
    if ans == "Remove" or "remove":
        removeAll()
    if ans == "alphabetize" or "Alphabetize":
        sorts()
    if ans== "count" or "Count":
        count()
    if ans == "exit" or "Exit":
        quit()


#Main
menu()
