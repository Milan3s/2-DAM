from typing import List


class Persona:
    """Clase base para representar a una persona."""
    def __init__(self, nombre: str, apellido: str):
        self.nombre = nombre
        self.apellido = apellido

    def __str__(self):
        return f"{self.nombre} {self.apellido}"


class Contacto(Persona):
    """Clase Contacto que hereda de Persona y añade teléfono y dirección."""
    def __init__(self, nombre: str, apellido: str, telefono: str, direccion: str):
        super().__init__(nombre, apellido)
        self.telefono = telefono
        self.direccion = direccion

    def __str__(self):
        return f"{super().__str__()} | Tel: {self.telefono} | Dirección: {self.direccion}"


class Agenda:
    """Clase Agenda para gestionar contactos."""
    def __init__(self):
        self.contactos: List[Contacto] = []

    def agregar_contacto(self, contacto: Contacto):
        """Agrega un nuevo contacto a la agenda."""
        self.contactos.append(contacto)
        print(f"Contacto agregado: {contacto}")

    def eliminar_contacto(self, nombre: str):
        """Elimina un contacto por nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                self.contactos.remove(contacto)
                print(f"Contacto eliminado: {contacto}")
                return
        print(f"Contacto con nombre {nombre} no encontrado.")

    def modificar_contacto(self, nombre: str, nuevo_telefono: str = None, nueva_direccion: str = None):
        """Modifica los datos de un contacto existente."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                if nuevo_telefono:
                    contacto.telefono = nuevo_telefono
                if nueva_direccion:
                    contacto.direccion = nueva_direccion
                print(f"Contacto modificado: {contacto}")
                return
        print(f"Contacto con nombre {nombre} no encontrado.")

    def buscar_contacto(self, nombre: str):
        """Busca un contacto por nombre."""
        for contacto in self.contactos:
            if contacto.nombre.lower() == nombre.lower():
                return contacto
        print(f"Contacto con nombre {nombre} no encontrado.")
        return None

    def listar_contactos(self):
        """Lista todos los contactos en formato HTML."""
        print(self._generar_html_listado())

    def _generar_html_listado(self):
        """Genera un listado HTML de los contactos."""
        html = "<html><body><h1>Lista de Contactos</h1><ul>"
        for contacto in self.contactos:
            html += f"<li>{contacto}</li>"
        html += "</ul></body></html>"
        return html


# Ejemplo de uso
if __name__ == "__main__":
    agenda = Agenda()

    # Crear contactos
    contacto1 = Contacto("Juan", "Pérez", "123456789", "Calle Falsa 123")
    contacto2 = Contacto("María", "Gómez", "987654321", "Avenida Siempreviva 456")

    # Agregar contactos
    agenda.agregar_contacto(contacto1)
    agenda.agregar_contacto(contacto2)

    # Listar contactos
    agenda.listar_contactos()

    # Buscar un contacto
    print(agenda.buscar_contacto("Juan"))

    # Modificar un contacto
    agenda.modificar_contacto("Juan", nuevo_telefono="111222333")

    # Eliminar un contacto
    agenda.eliminar_contacto("María")

    # Listar contactos nuevamente
    agenda.listar_contactos()

