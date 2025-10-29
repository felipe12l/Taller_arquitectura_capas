"""
Capa de Presentación - Interfaz de Usuario por Terminal
Responsabilidad: Interactuar con el usuario, mostrar menús y resultados
"""

from src.capa_negocio.gestor_matriculas import GestorMatriculas
from src.capa_negocio.gestor_cursos import GestorCursos
from src.capa_negocio.gestor_estudiantes import GestorEstudiantes
from src.auth.auth_service import AuthService
import sys
import os

# Agregar el directorio raíz al path para importaciones
sys.path.insert(0, os.path.abspath(
    os.path.join(os.path.dirname(__file__), '../..')))


class InterfazUsuario:
    """Clase que maneja la interacción con el usuario por terminal"""

    def __init__(self):
        """Inicializa los gestores de negocio"""
        self.gestor_estudiantes = GestorEstudiantes()
        self.gestor_cursos = GestorCursos()
        self.gestor_matriculas = GestorMatriculas()
        # Servicio de autenticación
        self.auth_service = AuthService()

        # Vincular los DAOs compartidos para que la matrícula pueda validar
        self.gestor_matriculas.vincular_daos(
            self.gestor_estudiantes.estudiante_dao,
            self.gestor_cursos.curso_dao
        )

    def limpiar_pantalla(self):
        """Limpia la pantalla de la terminal"""
        os.system('cls' if os.name == 'nt' else 'clear')

    def pausar(self):
        """Pausa la ejecución hasta que el usuario presione Enter"""
        input("\nPresione Enter para continuar...")

    def mostrar_menu_principal(self):
        """Muestra el menú principal del sistema"""
        print("\n" + "="*50)
        print("    SISTEMA ACADÉMICO - GESTIÓN UNIVERSITARIA")
        print("="*50)
        print("\n1. Gestión de Estudiantes")
        print("2. Gestión de Cursos")
        print("3. Gestión de Matrículas")
        print("4. Consultas y Listados")
        print("0. Salir")
        print("\n" + "-"*50)

    def menu_estudiantes(self):
        """Menú de gestión de estudiantes"""
        while True:
            self.limpiar_pantalla()
            print("\n" + "="*50)
            print("    GESTIÓN DE ESTUDIANTES")
            print("="*50)
            print("\n1. Registrar nuevo estudiante")
            print("2. Buscar estudiante por identificación")
            print("3. Listar todos los estudiantes")
            print("0. Volver al menú principal")
            print("\n" + "-"*50)

            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.registrar_estudiante()
            elif opcion == '2':
                self.buscar_estudiante()
            elif opcion == '3':
                self.listar_estudiantes()
            elif opcion == '0':
                break
            else:
                print("\n❌ Opción no válida")
                self.pausar()

    def registrar_estudiante(self):
        """Registra un nuevo estudiante"""
        print("\n" + "-"*50)
        print("    REGISTRAR NUEVO ESTUDIANTE")
        print("-"*50)

        nombre = input("\nNombre completo: ")
        identificacion = input("Identificación: ")
        carrera = input("Carrera: ")
        semestre = input("Semestre: ")

        exito, mensaje = self.gestor_estudiantes.registrar_estudiante(
            nombre, identificacion, carrera, semestre
        )

        if exito:
            print(f"\n✓ {mensaje}")
        else:
            print(f"\n❌ Error: {mensaje}")

        self.pausar()

    def buscar_estudiante(self):
        """Busca un estudiante por identificación"""
        print("\n" + "-"*50)
        print("    BUSCAR ESTUDIANTE")
        print("-"*50)

        identificacion = input("\nIdentificación del estudiante: ")

        estudiante, mensaje = self.gestor_estudiantes.buscar_estudiante(
            identificacion)

        if estudiante:
            print(f"\n✓ {mensaje}")
            print("\n" + "-"*50)
            print(f"Nombre:         {estudiante['nombre']}")
            print(f"Identificación: {estudiante['identificacion']}")
            print(f"Carrera:        {estudiante['carrera']}")
            print(f"Semestre:       {estudiante['semestre']}")
            print("-"*50)
        else:
            print(f"\n❌ {mensaje}")

        self.pausar()

    def listar_estudiantes(self):
        """Lista todos los estudiantes registrados"""
        print("\n" + "-"*50)
        print("    LISTADO DE ESTUDIANTES")
        print("-"*50)

        estudiantes = self.gestor_estudiantes.listar_estudiantes()

        if not estudiantes:
            print("\nNo hay estudiantes registrados")
        else:
            print(f"\nTotal de estudiantes: {len(estudiantes)}\n")
            for i, est in enumerate(estudiantes, 1):
                print(f"{i}. {est['nombre']}")
                print(
                    f"   ID: {est['identificacion']} | Carrera: {est['carrera']} | Semestre: {est['semestre']}")
                print()

        self.pausar()

    def menu_cursos(self):
        """Menú de gestión de cursos"""
        while True:
            self.limpiar_pantalla()
            print("\n" + "="*50)
            print("    GESTIÓN DE CURSOS")
            print("="*50)
            print("\n1. Registrar nuevo curso")
            print("2. Buscar curso por código")
            print("3. Listar todos los cursos")
            print("0. Volver al menú principal")
            print("\n" + "-"*50)

            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.registrar_curso()
            elif opcion == '2':
                self.buscar_curso()
            elif opcion == '3':
                self.listar_cursos()
            elif opcion == '0':
                break
            else:
                print("\n❌ Opción no válida")
                self.pausar()

    def registrar_curso(self):
        """Registra un nuevo curso"""
        print("\n" + "-"*50)
        print("    REGISTRAR NUEVO CURSO")
        print("-"*50)

        # Control de permisos en la capa de Autenticación
        if not self.auth_service.authorize('admin'):
            print("\n❌ Acceso denegado: se requiere rol 'admin' para registrar cursos")
            self.pausar()
            return

        codigo = input("\nCódigo del curso: ")
        nombre = input("Nombre del curso: ")
        creditos = input("Número de créditos: ")

        exito, mensaje = self.gestor_cursos.registrar_curso(
            codigo, nombre, creditos
        )

        if exito:
            print(f"\n✓ {mensaje}")
        else:
            print(f"\n❌ Error: {mensaje}")

        self.pausar()

    def buscar_curso(self):
        """Busca un curso por código"""
        print("\n" + "-"*50)
        print("    BUSCAR CURSO")
        print("-"*50)

        codigo = input("\nCódigo del curso: ")

        curso, mensaje = self.gestor_cursos.buscar_curso(codigo)

        if curso:
            print(f"\n✓ {mensaje}")
            print("\n" + "-"*50)
            print(f"Código:   {curso['codigo']}")
            print(f"Nombre:   {curso['nombre']}")
            print(f"Créditos: {curso['creditos']}")
            print("-"*50)
        else:
            print(f"\n❌ {mensaje}")

        self.pausar()

    def listar_cursos(self):
        """Lista todos los cursos registrados"""
        print("\n" + "-"*50)
        print("    LISTADO DE CURSOS")
        print("-"*50)

        cursos = self.gestor_cursos.listar_cursos()

        if not cursos:
            print("\nNo hay cursos registrados")
        else:
            print(f"\nTotal de cursos: {len(cursos)}\n")
            for i, curso in enumerate(cursos, 1):
                print(f"{i}. {curso['nombre']}")
                print(
                    f"   Código: {curso['codigo']} | Créditos: {curso['creditos']}")
                print()

        self.pausar()

    def menu_matriculas(self):
        """Menú de gestión de matrículas"""
        while True:
            self.limpiar_pantalla()
            print("\n" + "="*50)
            print("    GESTIÓN DE MATRÍCULAS")
            print("="*50)
            print("\n1. Matricular estudiante en curso")
            print("2. Listar todas las matrículas")
            print("0. Volver al menú principal")
            print("\n" + "-"*50)

            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.matricular_estudiante()
            elif opcion == '2':
                self.listar_matriculas()
            elif opcion == '0':
                break
            else:
                print("\n❌ Opción no válida")
                self.pausar()

    def matricular_estudiante(self):
        """Matricula un estudiante en un curso"""
        print("\n" + "-"*50)
        print("    MATRICULAR ESTUDIANTE")
        print("-"*50)

        identificacion = input("\nIdentificación del estudiante: ")
        codigo_curso = input("Código del curso: ")

        exito, mensaje = self.gestor_matriculas.matricular_estudiante(
            identificacion, codigo_curso
        )

        if exito:
            print(f"\n✓ {mensaje}")
        else:
            print(f"\n❌ Error: {mensaje}")

        self.pausar()

    def listar_matriculas(self):
        """Lista todas las matrículas registradas"""
        print("\n" + "-"*50)
        print("    LISTADO DE MATRÍCULAS")
        print("-"*50)

        matriculas = self.gestor_matriculas.listar_matriculas()

        if not matriculas:
            print("\nNo hay matrículas registradas")
        else:
            print(f"\nTotal de matrículas: {len(matriculas)}\n")
            for i, mat in enumerate(matriculas, 1):
                est = mat['estudiante']
                curso = mat['curso']
                print(
                    f"{i}. Estudiante: {est['nombre']} (ID: {est['identificacion']})")
                print(
                    f"   Curso: {curso['nombre']} (Código: {curso['codigo']}) - {curso['creditos']} créditos")
                print()

        self.pausar()

    def menu_consultas(self):
        """Menú de consultas y listados generales"""
        while True:
            self.limpiar_pantalla()
            print("\n" + "="*50)
            print("    CONSULTAS Y LISTADOS")
            print("="*50)
            print("\n1. Listar todos los estudiantes")
            print("2. Listar todos los cursos")
            print("3. Listar todas las matrículas")
            print("0. Volver al menú principal")
            print("\n" + "-"*50)

            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.listar_estudiantes()
            elif opcion == '2':
                self.listar_cursos()
            elif opcion == '3':
                self.listar_matriculas()
            elif opcion == '0':
                break
            else:
                print("\n❌ Opción no válida")
                self.pausar()

    def ejecutar(self):
        """Método principal que ejecuta la aplicación"""
        # Solicitar autenticación antes de permitir operaciones
        if not self._login_screen():
            print("Saliendo del sistema.")
            return

        while True:
            self.limpiar_pantalla()
            self.mostrar_menu_principal()

            usuario = self.auth_service.current_user or {'username': '---', 'role': '---'}
            print(f"\nUsuario: {usuario.get('username')} (rol: {usuario.get('role')})")
            print("9. Cerrar sesión")
            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                self.menu_estudiantes()
            elif opcion == '2':
                self.menu_cursos()
            elif opcion == '3':
                self.menu_matriculas()
            elif opcion == '4':
                self.menu_consultas()
            elif opcion == '9':
                self.auth_service.logout()
                print("Sesión cerrada.")
                self.pausar()
                if not self._login_screen():
                    print("Saliendo del sistema.")
                    return
            elif opcion == '0':
                print("\n¡Gracias por usar el Sistema Académico!")
                print("Hasta pronto.\n")
                break
            else:
                print("\n❌ Opción no válida")
                self.pausar()

    def _login_screen(self):
        """Pantalla que solicita inicio de sesión o registro de usuario.

        Returns True si se autenticó un usuario, False para salir.
        """
        while True:
            self.limpiar_pantalla()
            print("\n" + "="*50)
            print("    AUTENTICACIÓN - SISTEMA ACADÉMICO")
            print("="*50)
            print("\n1. Iniciar sesión")
            print("2. Registrar nuevo usuario")
            print("0. Salir")

            opcion = input("\nSeleccione una opción: ")

            if opcion == '1':
                username = input("\nUsuario: ")
                password = input("Contraseña: ")
                exito, msg = self.auth_service.login(username, password)
                if exito:
                    print(f"\n✓ {msg}")
                    self.pausar()
                    return True
                else:
                    print(f"\n❌ {msg}")
                    self.pausar()
            elif opcion == '2':
                print("\nRegistro de nuevo usuario")
                username = input("Usuario: ")
                password = input("Contraseña: ")
                role = input("Rol (admin/user). Por defecto 'user': ")
                role = role.strip() or 'user'
                exito, msg = self.auth_service.register_user(username, password, role)
                if exito:
                    print(f"\n✓ {msg}")
                else:
                    print(f"\n❌ {msg}")
                self.pausar()
            elif opcion == '0':
                return False
            else:
                print("\n❌ Opción no válida")
                self.pausar()


def main():
    """Función principal para iniciar la aplicación"""
    interfaz = InterfazUsuario()
    interfaz.ejecutar()


if __name__ == "__main__":
    main()
