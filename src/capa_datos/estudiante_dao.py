"""
Capa de Datos - Estudiante DAO (Data Access Object)
Responsabilidad: Gestionar el almacenamiento y recuperación de estudiantes
"""


class EstudianteDAO:
    """Clase para gestionar el acceso a datos de estudiantes"""

    def __init__(self):
        """Inicializa el almacenamiento en memoria"""
        self.estudiantes = []

    def guardar(self, estudiante):
        """
        Guarda un estudiante en el almacenamiento

        Args:
            estudiante (dict): Diccionario con datos del estudiante

        Returns:
            bool: True si se guardó correctamente
        """
        self.estudiantes.append(estudiante)
        return True

    def buscar_por_identificacion(self, identificacion):
        """
        Busca un estudiante por su identificación

        Args:
            identificacion (str): Identificación del estudiante

        Returns:
            dict o None: Estudiante encontrado o None
        """
        for estudiante in self.estudiantes:
            if estudiante['identificacion'] == identificacion:
                return estudiante
        return None

    def listar_todos(self):
        """
        Obtiene todos los estudiantes registrados

        Returns:
            list: Lista de estudiantes
        """
        return self.estudiantes.copy()

    def existe(self, identificacion):
        """
        Verifica si existe un estudiante con la identificación dada

        Args:
            identificacion (str): Identificación a verificar

        Returns:
            bool: True si existe, False en caso contrario
        """
        return self.buscar_por_identificacion(identificacion) is not None
