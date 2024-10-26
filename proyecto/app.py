from data.productos import ProductoFactory
from business.pedido import Pedido
from business.decorators import EnvolturaRegaloDecorator, EnvioUrgenteDecorator
from utils.cliente import Cliente

def main():
    producto_factory = ProductoFactory()
    producto = producto_factory.crear_producto("electronico")
    print(producto.crear())

    pedido = Pedido()
    cliente1 = Cliente("Juan")
    cliente2 = Cliente("María")
    pedido.agregar_cliente(cliente1)
    pedido.agregar_cliente(cliente2)

    pedido_con_envio_urgente = EnvioUrgenteDecorator(pedido)
    pedido_con_envio_urgente_y_regalo = EnvolturaRegaloDecorator(pedido_con_envio_urgente)

    pedido_con_envio_urgente_y_regalo.procesar_pedido()

if __name__ == "__main__":
    main()
