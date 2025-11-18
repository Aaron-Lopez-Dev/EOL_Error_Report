import startProdLine

vinCount = int(input("How many cars are we making?: ")) + 1

while vinCount <= 0:
     print("You have entered letters or a negative number")
     vinCount = int(input("How many cars?: ")) + 1


startProdLine.startProdLine(vinCount)