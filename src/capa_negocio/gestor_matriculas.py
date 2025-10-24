"""
Capa de Negocio - Gestor de Matrículas
Responsabilidad: Implementar reglas de negocio y validaciones para matrículas
"""

from ..capa_datos.matricula_dao import MatriculaDAO
from ..capa_datos.estudiante_dao import EstudianteDAO
from ..capa_datos.curso_dao import CursoDAO


class GestorMatriculas:
    """Clase que implementa la lógica de negocio para matrículas"""

    def __init__(self):
        """Inicializa el gestor con sus DAOs correspondientes"""
        self.matricula_dao = MatriculaDAO()
        self.estudiante_dao = EstudianteDAO()
        self.curso_dao = CursoDAO()

    def vincular_daos(self, estudiante_dao, curso_dao):
        """
        Vincula los DAOs de estudiantes y cursos existentes

        Args:
            estudiante_dao: DAO de estudiantes compartido
            curso_dao: DAO de cursos compartido
        """
        self.estudiante_dao = estudiante_dao
        self.curso_dao = curso_dao

    def matricular_estudiante(self, identificacion_estudiante, codigo_curso):
        """
        Matricula un estudiante en un curso aplicando validaciones de negocio

        Args:
            identificacion_estudiante (str): Identificación del estudiante
            codigo_curso (str): Código del curso

        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        # Validaciones de entrada
        if not identificacion_estudiante or not identificacion_estudiante.strip():
            return False, "Debe proporcionar una identificación de estudiante válida"

        if not codigo_curso or not codigo_curso.strip():
            return False, "Debe proporcionar un código de curso válido"

        identificacion_estudiante = identificacion_estudiante.strip()
        codigo_curso = codigo_curso.strip()

        # Validar que el estudiante existe
        if not self.estudiante_dao.existe(identificacion_estudiante):
            return False, f"No existe estudiante con identificación {identificacion_estudiante}"

        # Validar que el curso existe
        if not self.curso_dao.existe(codigo_curso):
            return False, f"No existe curso con código {codigo_curso}"

        # Validar que no esté ya matriculado
        if self.matricula_dao.existe_matricula(identificacion_estudiante, codigo_curso):
            return False, f"El estudiante ya está matriculado en el curso {codigo_curso}"

        # Crear la matrícula
        matricula = {
            'identificacion_estudiante': identificacion_estudiante,
            'codigo_curso': codigo_curso
        }

        # Guardar en la capa de datos
        self.matricula_dao.guardar(matricula)
        return True, "Matrícula realizada exitosamente"

    def listar_matriculas(self):
        """
        Obtiene todas las matrículas registradas con información detallada

        Returns:
            list: Lista de matrículas con datos de estudiante y curso
        """
        matriculas = self.matricula_dao.listar_todas()
        matriculas_detalladas = []

        for matricula in matriculas:
            estudiante = self.estudiante_dao.buscar_por_identificacion(
                matricula['identificacion_estudiante']
            )
            curso = self.curso_dao.buscar_por_codigo(
                matricula['codigo_curso']
            )

            matriculas_detalladas.append({
                'estudiante': estudiante,
                'curso': curso
            })

        return matriculas_detalladas
