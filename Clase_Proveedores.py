
from BD import tabla_proveedores
from BD import conectar
class Proveedor():
    def __init__(self, Id_proveedor,nombre,telefono, direccion, estado):
        self.Id_proveedor=Id_proveedor
        self.nombre=nombre
        self.telefono=telefono
        self.direccion=direccion
        self.estado=estado
        tabla_proveedores()


    def agregar_proveedor(self):
        conexion=conectar()
        cursor=conexion.cursor()
        nombre=input("Ingresar el nombre del proveedor:  ")
        telefono=input("Ingresar el telefono:  ")
        direccion=input("Ingrese la direccion:  ")
        estado=input("Ingrese el estado del proveedor" \
        "1- activo" \
        "2- Inactivo" \
        "--------------" \
        "")
        cursor.execute("""
            insert into proveedores (nombre,telefono,direccion,estado) values (?,?,?,?)""",self.nombre, self.telefono, self.direccion,self.estado)
        print(f"El proveedor {self.nombre} fué agregado correctamente :)")

        conexion.commit()
        conexion.close()

    def eliminar_proveedor(self):
        conexion=conectar()
        cursor=conexion.cursor()
        proveedor=input("ingrese el Id del proveedor que desea eliminar: ")
        cursor.execute("delete from proveedores where id_proveedor= ?",(proveedor))
        conexion.commit()
        conexion.close()
        print(f"El proveedor {self.nombre} fue eliminado correctamente")

    def ejecucion_modificacion_prov(self,nombre_columna,dato,proveedor):
        conexion=conectar()
        cursor=conexion.cursor()
        cursor.execute("""update proveedores set {nombre_columna}= ? where Id_proveedor= ?""",dato,proveedor)
        print(f"El atributo{nombre_columna} fue modificado ")
        conexion.commit()
        conexion.close() 

    def modificar_proveedores(self):
        conexion=conectar()
        cursor=conexion.cursor()
        print ("--ATRIBUTOS PARA MODIFICAR--")
        print ("1-Nombre")
        print ("2-Telefono")
        print ("3-Dirección")
        print ("4-Estado")
        opcion=input("Ingrese el numero del atributo que desea modificar:  ")
        proveedor=input("Ingrese el Id del proveedor el cual desea modificar: ")
        dato=input("Ingresar el nuevo valor: ")
        columnas={"1":"Nombre", "2":"Telefono","3":"Direccion","4":"Estado"}
        if opcion in columnas:
            nombre_columna=columnas[opcion]
      

    def mostrar_proveedores(self):
        conexion=conectar()
        cursor=conexion.cursor()
        cursor.execute(""" select * from proveedores""")
        proveedores=list(cursor.fetchall())
        for self.id_proveedor, self.nombre, self.telefono, self.direccion,self.estado in proveedores:
            print (f"Id:{self.id_proveedor}- Nombre: {self.nombre}- Telefono:{self.telefono}- Dirección:{self.direccion}-Estado:{self.estado}")
        
        conexion.close()

            

    
