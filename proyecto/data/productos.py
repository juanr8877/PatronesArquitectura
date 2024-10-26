from abc import ABC, abstractmethod

class Producto(ABC):
    @abstractmethod
    def crear(self):
        pass

class ProductoElectronico(Producto):
    def crear(self):
        return "Producto Electrónico creado."

class ProductoAlimento(Producto):
    def crear(self):
        return "Producto de Alimento creado."

class ProductoFactory:
    @staticmethod
    def crear_producto(tipo_producto):
        if tipo_producto == "electronico":
            return ProductoElectronico()
        elif tipo_producto == "alimento":
            return ProductoAlimento()
        else:
            raise ValueError("Tipo de producto no soportado.")
