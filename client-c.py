inventoryA = 0
inventoryB = 0
inventoryC = 0

while True:
    scan = input("Please scan item: ")
    if scan == 'A':
        inventoryA += 2
        if inventoryA == 50:
            print("Time for a new box!")
            inventoryA = 0
    elif scan == 'B':
        inventoryB += 2
        if inventoryB == 50:
            print("Time for a new box!")
            inventoryB = 0
    elif scan == 'C':
        inventoryC += 2
        if inventoryC == 50:
            print("Time for a new box!")
            inventoryC = 0
    else:
        print("This item doesn't belong here")
        break