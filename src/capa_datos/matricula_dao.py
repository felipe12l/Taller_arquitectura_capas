"""
Capa de Datos - Matrícula DAO (Data Access Object)
Responsabilidad: Gestionar el almacenamiento y recuperación de matrículas
"""


class MatriculaDAO:
    """Clase para gestionar el acceso a datos de matrículas"""

    def __init__(self):
        """Inicializa el almacenamiento en memoria"""
        self.matriculas = []

    def guardar(self, matricula):
        """
        Guarda una matrícula en el almacenamiento

        Args:
            matricula (dict): Diccionario con datos de la matrícula

        Returns:
            bool: True si se guardó correctamente
        """
        self.matriculas.append(matricula)
        return True

    def listar_todas(self):
        """
        Obtiene todas las matrículas registradas

        Returns:
            list: Lista de matrículas
        """
        return self.matriculas.copy()

    def buscar_por_estudiante_y_curso(self, identificacion_estudiante, codigo_curso):
        """
        Busca una matrícula específica por estudiante y curso

        Args:
            identificacion_estudiante (str): Identificación del estudiante
            codigo_curso (str): Código del curso

        Returns:
            dict o None: Matrícula encontrada o None
        """
        for matricula in self.matriculas:
            if (matricula['identificacion_estudiante'] == identificacion_estudiante and
                    matricula['codigo_curso'] == codigo_curso):
                return matricula
        return None

    def existe_matricula(self, identificacion_estudiante, codigo_curso):
        """
        Verifica si existe una matrícula para un estudiante en un curso

        Args:
            identificacion_estudiante (str): Identificación del estudiante
            codigo_curso (str): Código del curso

        Returns:
            bool: True si existe, False en caso contrario
        """
        return self.buscar_por_estudiante_y_curso(identificacion_estudiante, codigo_curso) is not None
