from BD import tabla_marcas
from BD import conectar

class Marca():  
    def __init__(self,id_marca, nombre):
        self.__id_marca=id_marca
        self.nombre=nombre
        tabla_marcas()
    
    @property
    def marca (self):
        return self.__id_marca
    
    @marca.setter
    def marca(self, nueva_marca):
        self.__id_marca=nueva_marca


    def agregar_marca(self):
        nombre=input("Ingresar el nombre de la nueva marca")
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""inser into marcas(nombre) values (?)""", nombre)
            conexion.commit()
            print("La nueva marca fué agregada correctamente")
        except Exception as e:
            print("Error al agregar la marca",e)
        finally:
            conexion.close()
        

    def eliminar_marca(self):
        id=input("Ingresar el ID de la marca que desea eliminar")
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""delete from categorias where id_categoria= ?""", id)
            conexion.commit()
            print("La marca se eliminó correctamente")
        except Exception as e:
            print ("Error al eliminar la marca", e)
        finally:
             conexion.close()
        
    
    def modificar_marca(self):
        id=input("Ingresar el ID de a marca que desea modificar.")
        nombre=input("Ingresar su nuevo nombre")
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute(""" update marcas set nombre= ? where id_marca= ?""", nombre, id)
            conexion.commit()
            print("Se modificó correctamente")
        except Exception as e:
            print("Error al modificar la marca",e)
        finally:
            conexion.close()
      
    def listar_marca(self):
        print("--LISTA DE MARCAS--")
        try:
            conexion=conectar()
            cursor=conexion.cursor()
            cursor.execute("""select * from marcas""")
            marcas=list(cursor.fetchall())
            if not marcas:
                print("No hay marcas registradas")
            else:
                for id_marca, nombre in marcas:
                    print(f"ID: {id_marca} - Nombre:{nombre}")
        except Exception as e:
            print("Error al listas las marcas",e)
        finally:
            conexion.close()