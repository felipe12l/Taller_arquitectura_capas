"""
Capa de Negocio - Gestor de Estudiantes
Responsabilidad: Implementar reglas de negocio y validaciones para estudiantes
"""

from ..capa_datos.estudiante_dao import EstudianteDAO


class GestorEstudiantes:
    """Clase que implementa la lógica de negocio para estudiantes"""

    def __init__(self):
        """Inicializa el gestor con su DAO correspondiente"""
        self.estudiante_dao = EstudianteDAO()

    def registrar_estudiante(self, nombre, identificacion, carrera, semestre):
        """
        Registra un nuevo estudiante aplicando validaciones de negocio

        Args:
            nombre (str): Nombre del estudiante
            identificacion (str): Identificación única del estudiante
            carrera (str): Carrera que cursa
            semestre (int): Semestre actual

        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        # Validaciones de negocio
        if not nombre or not nombre.strip():
            return False, "El nombre no puede estar vacío"

        if not identificacion or not identificacion.strip():
            return False, "La identificación no puede estar vacía"

        if not carrera or not carrera.strip():
            return False, "La carrera no puede estar vacía"

        try:
            semestre_num = int(semestre)
            if semestre_num <= 0:
                return False, "El semestre debe ser un número positivo"
        except ValueError:
            return False, "El semestre debe ser un número válido"

        # Verificar duplicados
        if self.estudiante_dao.existe(identificacion):
            return False, f"Ya existe un estudiante con la identificación {identificacion}"

        # Crear el estudiante
        estudiante = {
            'nombre': nombre.strip(),
            'identificacion': identificacion.strip(),
            'carrera': carrera.strip(),
            'semestre': semestre_num
        }

        # Guardar en la capa de datos
        self.estudiante_dao.guardar(estudiante)
        return True, "Estudiante registrado exitosamente"

    def buscar_estudiante(self, identificacion):
        """
        Busca un estudiante por su identificación

        Args:
            identificacion (str): Identificación del estudiante

        Returns:
            tuple: (encontrado: dict o None, mensaje: str)
        """
        if not identificacion or not identificacion.strip():
            return None, "Debe proporcionar una identificación válida"

        estudiante = self.estudiante_dao.buscar_por_identificacion(
            identificacion.strip())

        if estudiante:
            return estudiante, "Estudiante encontrado"
        else:
            return None, f"No se encontró estudiante con identificación {identificacion}"

    def listar_estudiantes(self):
        """
        Obtiene todos los estudiantes registrados

        Returns:
            list: Lista de estudiantes
        """
        return self.estudiante_dao.listar_todos()
