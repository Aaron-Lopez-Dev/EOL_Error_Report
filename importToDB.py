import sqlite3, json
import globals

def createDatabase():
    db_file = './completedCars.db'
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            vin TEXT PRIMARY KEY,
            completed INT,
            errors INT,
            torque_values TEXT)  ;         
    ''')

    insertInitialSQL = '''
    INSERT INTO vehicles (vin, torque_values)
    VALUES (:vin, :torque_values);
    '''
    updateColumnError = '''
    UPDATE vehicles
    SET completed = 0, errors = 1
    WHERE vin = :vin;
    '''
    updateColumnCompleted = '''
    UPDATE vehicles
    SET completed = 1, errors = 0
    WHERE vin = :vin;
    '''
    for i, data in globals.completedCarsUnfused.items():
        row = {
            "vin": i,
            "torque_values": json.dumps(data)
        }
        c.execute(insertInitialSQL, row)

        if i in globals.completedCarsWithErrors.keys():
            c.execute(updateColumnError,{"vin": i})
        else:
            c.execute(updateColumnCompleted,{"vin": i})

    conn.commit()
    
    
