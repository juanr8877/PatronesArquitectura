class Cliente:
    def __init__(self, nombre):
        self.nombre = nombre

    def actualizar(self, mensaje):
        print(f"Notificación para {self.nombre}: {mensaje}")
