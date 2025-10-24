"""
Capa de Datos - Curso DAO (Data Access Object)
Responsabilidad: Gestionar el almacenamiento y recuperación de cursos
"""


class CursoDAO:
    """Clase para gestionar el acceso a datos de cursos"""

    def __init__(self):
        """Inicializa el almacenamiento en memoria"""
        self.cursos = []

    def guardar(self, curso):
        """
        Guarda un curso en el almacenamiento

        Args:
            curso (dict): Diccionario con datos del curso

        Returns:
            bool: True si se guardó correctamente
        """
        self.cursos.append(curso)
        return True

    def buscar_por_codigo(self, codigo):
        """
        Busca un curso por su código

        Args:
            codigo (str): Código del curso

        Returns:
            dict o None: Curso encontrado o None
        """
        for curso in self.cursos:
            if curso['codigo'] == codigo:
                return curso
        return None

    def listar_todos(self):
        """
        Obtiene todos los cursos registrados

        Returns:
            list: Lista de cursos
        """
        return self.cursos.copy()

    def existe(self, codigo):
        """
        Verifica si existe un curso con el código dado

        Args:
            codigo (str): Código a verificar

        Returns:
            bool: True si existe, False en caso contrario
        """
        return self.buscar_por_codigo(codigo) is not None
