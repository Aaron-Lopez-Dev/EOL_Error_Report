import checkTorqueValues
import globals
import random


def startProdLine(vinCount):

    finalTorque = float(9.8)
    boltD = float(.008)
    vin = 0
    torqueValues = []

    for i in range(1, vinCount):
            for j in range(1, 8):
                boltK = float(globals.bugValues[random.randint(0,(len(globals.bugValues)-1))])

                force = finalTorque / (boltK * boltD)
                torqueValues.append(f"Bolt {j}:" f" {int(force)}")

            globals.completedCarsUnfused[f"VIN: {i}"] = {"torqueValues" : torqueValues.copy()}
            torqueValues.clear()

    vin = vin + 1

    checkTorqueValues.checkTorqueValues()


"""
Force = Torque/(K * D)

K = Nut Factor 
F = Bolt Tension(Force)
D = Diameter (METERS) 


T = 9.8Nm 
K = .18
F = 6,805 N (9.8nm)
D = M8: .008m 

2021-2024 MY 
9.8nm Torque for fender Bolts & 7 Bolts Total Secure Fender
"""