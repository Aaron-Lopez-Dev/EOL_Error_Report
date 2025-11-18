import sqlite3, json
import globals

def createDatabase():
    db_file = './completedCars.db'
    conn = sqlite3.connect(db_file)

    c = conn.cursor()
    
    c.execute('''
        CREATE TABLE IF NOT EXISTS vehicles (
            vin TEXT PRIMARY KEY,
            completed TEXT,
            errors TEXT,
            torque_values TEXT)  ;         
    ''')

    insertInitialSQL = '''
    INSERT INTO vehicles (vin, torque_values)
    VALUES (:vin, :torque_values);
    '''
    updateColumnError = '''
    UPDATE vehicles
    SET completed = FALSE, errors = TRUE
    WHERE vin = :vin;
    '''
    updateColumnCompleted = '''
    UPDATE vehicles
    SET completed = TRUE, errors = FALSE
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
    
    
