from abc import ABC, abstractmethod

class PedidoDecorator(ABC):
    def __init__(self, pedido):
        self._pedido = pedido

    @abstractmethod
    def procesar_pedido(self):
        pass

class EnvolturaRegaloDecorator(PedidoDecorator):
    def procesar_pedido(self):
        print("Añadiendo envoltura de regalo...")
        self._pedido.procesar_pedido()

class EnvioUrgenteDecorator(PedidoDecorator):
    def procesar_pedido(self):
        print("Añadiendo envío urgente...")
        self._pedido.procesar_pedido()
