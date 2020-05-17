todo = ["Clean room", "Eat Lunch","Get groceries"]

def addnew():
    add = input("Add to list: ")
    todo.append(add)

def completeitem():
    remove = int(input("Index of item done:"))
    print(todo[remove]+" removed")
    print("")
    todo.remove(todo[remove])
    print("updated list:")
    printlist()

def printlist():
    listlen = len(todo)
    for x in range(listlen):
        print("-"+todo[x])

completeitem()
printlist()
