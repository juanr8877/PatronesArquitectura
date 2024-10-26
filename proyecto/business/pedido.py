class Pedido:
    def __init__(self):
        self.clientes = []

    def agregar_cliente(self, cliente):
        self.clientes.append(cliente)

    def remover_cliente(self, cliente):
        self.clientes.remove(cliente)

    def notificar_clientes(self, mensaje):
        for cliente in self.clientes:
            cliente.actualizar(mensaje)

    def procesar_pedido(self):
        print("Procesando el pedido...")
        self.notificar_clientes("Su pedido está listo para el envío.")
