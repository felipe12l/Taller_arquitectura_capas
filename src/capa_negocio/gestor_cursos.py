"""
Capa de Negocio - Gestor de Cursos
Responsabilidad: Implementar reglas de negocio y validaciones para cursos
"""

from ..capa_datos.curso_dao import CursoDAO


class GestorCursos:
    """Clase que implementa la lógica de negocio para cursos"""

    def __init__(self):
        """Inicializa el gestor con su DAO correspondiente"""
        self.curso_dao = CursoDAO()

    def registrar_curso(self, codigo, nombre, creditos):
        """
        Registra un nuevo curso aplicando validaciones de negocio

        Args:
            codigo (str): Código único del curso
            nombre (str): Nombre del curso
            creditos (int): Número de créditos

        Returns:
            tuple: (éxito: bool, mensaje: str)
        """
        # Validaciones de negocio
        if not codigo or not codigo.strip():
            return False, "El código no puede estar vacío"

        if not nombre or not nombre.strip():
            return False, "El nombre no puede estar vacío"

        try:
            creditos_num = int(creditos)
            if creditos_num <= 0:
                return False, "Los créditos deben ser un número positivo"
        except ValueError:
            return False, "Los créditos deben ser un número válido"

        # Verificar duplicados
        if self.curso_dao.existe(codigo):
            return False, f"Ya existe un curso con el código {codigo}"

        # Crear el curso
        curso = {
            'codigo': codigo.strip(),
            'nombre': nombre.strip(),
            'creditos': creditos_num
        }

        # Guardar en la capa de datos
        self.curso_dao.guardar(curso)
        return True, "Curso registrado exitosamente"

    def buscar_curso(self, codigo):
        """
        Busca un curso por su código

        Args:
            codigo (str): Código del curso

        Returns:
            tuple: (encontrado: dict o None, mensaje: str)
        """
        if not codigo or not codigo.strip():
            return None, "Debe proporcionar un código válido"

        curso = self.curso_dao.buscar_por_codigo(codigo.strip())

        if curso:
            return curso, "Curso encontrado"
        else:
            return None, f"No se encontró curso con código {codigo}"

    def listar_cursos(self):
        """
        Obtiene todos los cursos registrados

        Returns:
            list: Lista de cursos
        """
        return self.curso_dao.listar_todos()
