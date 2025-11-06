from BD import tabla_pedidos
from Clase_Detalle import tabla_detalle_pedidos
from Clase_Proveedores import Proveedor 
from BD import conectar


class Pedido():
    def __init__(self, id_pedidos=None,fecha_pedido=None, fecha_entrega=None, total=0,id_proveedor=None):
        self.id_pedido=id_pedidos
        self.fecha_pedido=fecha_pedido
        self.fecha_entrega=fecha_entrega
        self.total=total
        self.proveedor1=Proveedor(id_proveedor)
        tabla_pedidos()

    def agregar_pedido(self):
        print("--REALIZAR PEDIDO--")
        fecha_pedido = input("Ingrese fecha del pedido (AAAA-MM-DD): ")
        fecha_entrega = input("Ingrese fecha de entrega (AAAA-MM-DD): ")
        id_proveedor = input("Ingrese ID del proveedor: ")
        total = input("Ingrese total del pedido: ")

        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("""
                INSERT INTO Pedidos (fecha_pedido, fecha_entrega, id_prov, total)
                VALUES (?, ?, ?, ?)
            """, (fecha_pedido, fecha_entrega, id_proveedor, total))
            conexion.commit()
            print("Pedido realizado y guardado correctamente.")
        except Exception as e:
            print("Error al realizar el pedido:", e)
        finally:
            conexion.close()

    
    def listar_pedidos(self):
        print("--LISTA DE PEDIDOS--")
        try:
            conexion = conectar()
            cursor = conexion.cursor()
            cursor.execute("SELECT * FROM Pedidos")
            pedidos = list(cursor.fetchall())

            if not pedidos:
                print("No hay pedidos registrados.")
            else:
                for p in pedidos:
                    print(f"ID: {p[0]} | Fecha Pedido: {p[1]} | Fecha Entrega: {p[2]} | Total: ${p[3]} | ID Proveedor: {p[4]}")
        except Exception as e:
            print("Error al listar los pedidos:", e)
        finally:
            conexion.close()

        


    


