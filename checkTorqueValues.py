import json, globals, importToDB


def checkTorqueValues():
    vehicles = globals.completedCarsUnfused
    failures = False
    for vin, data in vehicles.items():
        appliedTorque = data["torqueValues"]

        for i, value in enumerate(appliedTorque):

            if int(value.split(":")[1]) < 6800:
                failures = True
                if vin in globals.completedCarsWithErrors:
                    globals.completedCarsWithErrors[vin].append(value.split(":")[0])
                else:
                    globals.completedCarsWithErrors[vin] = [value.split(":")[0]]
     
    if failures == False:
        print("All VINs Created Successfully\n")
        print(json.dumps(globals.completedCarsUnfused, indent=4))
    else:
        print("EOL Report | VINs NEED ATTENTION") 
        print(json.dumps(globals.completedCarsWithErrors, indent=4))

    importToDB.createDatabase()