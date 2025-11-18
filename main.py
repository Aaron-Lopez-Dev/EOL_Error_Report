import production, os

if os.path.exists("./completedCars.db"):
     os.remove("./completedCars.db")

vinCount = int(input("How many cars are we making?: ")) + 1

while vinCount <= 0:
     print("You have entered letters or a negative number")
     vinCount = int(input("How many cars?: ")) + 1


production.startProdLine(vinCount)