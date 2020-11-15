def insertardatos(clave,descripcion,cantidad,precio,tiempo):
    try:
        with sqlite3.connect("Ventas.db") as conn:
            c = conn.cursor()
            c.execute("CREATE TABLE IF NOT EXISTS registro (clave INTEGER PRIMARY KEY, descripcion TEXT NOT NULL,cantidad INTEGER NOT NULL,precio INTEGER NOT NULL,tiempo TEXT not null);")
            valores={"clave":clave,"descripcion":descripcion,"cantidad":cantidad,"precio":precio,"tiempo":tiempo}
            c.execute("INSERT INTO registro VALUES (:clave,:descripcion,:cantidad,:precio,:tiempo)",valores)
    except Error as e:
        print("-"*30)
        print(f"ERROR :{e}")
        print("No se registro el registro")
        print("-"*30)
        
def validacion(fecha):
    try:
        contador=0
        with sqlite3.connect("Ventas.db") as conn:
            c = conn.cursor()
            valor={"tiempo":fecha}
            c.execute("SELECT * FROM registro WHERE tiempo = :tiempo" , valor)
            registros=c.fetchall()
            
            
            for clave,descripcion,cantidad,precio,tiempo in registros:
                contador=contador+1
                print(f"CLAVE: {clave}")
                print(f"DESCRIPCION: {descripcion}")
                print(f"CANTIDAD: {cantidad}")
                print(f"PRECIO: {precio}")
                print(f"TIEMPO: {tiempo}")
                print("*"*40)
                
            if contador==0:
                print(f"No se ha registrado ninguna registro con esta fecha : {fecha}")
                
    except Error as e:
        print (e)