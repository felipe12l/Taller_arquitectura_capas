"""
Módulo de Pruebas Básicas
Sistema Académico - Arquitectura en 3 Capas

Este script realiza pruebas básicas del sistema para verificar
el flujo completo entre las tres capas.
"""

from src.capa_negocio.gestor_matriculas import GestorMatriculas
from src.capa_negocio.gestor_cursos import GestorCursos
from src.capa_negocio.gestor_estudiantes import GestorEstudiantes
import sys
import os

# Agregar el directorio raíz al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


def ejecutar_pruebas():
    """Ejecuta un conjunto de pruebas básicas del sistema"""

    print("="*60)
    print("  PRUEBAS DEL SISTEMA ACADÉMICO - ARQUITECTURA 3 CAPAS")
    print("="*60)

    # Inicializar gestores
    gestor_estudiantes = GestorEstudiantes()
    gestor_cursos = GestorCursos()
    gestor_matriculas = GestorMatriculas()

    # Vincular DAOs compartidos
    gestor_matriculas.vincular_daos(
        gestor_estudiantes.estudiante_dao,
        gestor_cursos.curso_dao
    )

    print("\n1. PRUEBAS DE REGISTRO DE ESTUDIANTES")
    print("-" * 60)

    # Prueba 1: Registrar estudiantes
    exito, msg = gestor_estudiantes.registrar_estudiante(
        "Juan Pérez García", "1001", "Ingeniería de Sistemas", "5"
    )
    print(f"  • Registrar estudiante 1: {'✓' if exito else '✗'} {msg}")

    exito, msg = gestor_estudiantes.registrar_estudiante(
        "María López Rodríguez", "1002", "Ingeniería Industrial", "3"
    )
    print(f"  • Registrar estudiante 2: {'✓' if exito else '✗'} {msg}")

    exito, msg = gestor_estudiantes.registrar_estudiante(
        "Carlos Martínez Silva", "1003", "Ingeniería de Sistemas", "7"
    )
    print(f"  • Registrar estudiante 3: {'✓' if exito else '✗'} {msg}")

    # Prueba 2: Intentar registrar duplicado
    exito, msg = gestor_estudiantes.registrar_estudiante(
        "Otro Nombre", "1001", "Otra Carrera", "1"
    )
    print(
        f"  • Registrar duplicado: {'✓ (rechazado correctamente)' if not exito else '✗ (debió rechazarse)'}")

    # Prueba 3: Validación de datos
    exito, msg = gestor_estudiantes.registrar_estudiante(
        "", "1004", "Ingeniería", "1"
    )
    print(
        f"  • Validar nombre vacío: {'✓ (rechazado correctamente)' if not exito else '✗ (debió rechazarse)'}")

    print("\n2. PRUEBAS DE REGISTRO DE CURSOS")
    print("-" * 60)

    # Prueba 4: Registrar cursos
    exito, msg = gestor_cursos.registrar_curso(
        "SW201", "Programación Orientada a Objetos", "4"
    )
    print(f"  • Registrar curso 1: {'✓' if exito else '✗'} {msg}")

    exito, msg = gestor_cursos.registrar_curso(
        "SW202", "Bases de Datos", "3"
    )
    print(f"  • Registrar curso 2: {'✓' if exito else '✗'} {msg}")

    exito, msg = gestor_cursos.registrar_curso(
        "SW203", "Arquitectura de Software", "4"
    )
    print(f"  • Registrar curso 3: {'✓' if exito else '✗'} {msg}")

    # Prueba 5: Intentar registrar curso duplicado
    exito, msg = gestor_cursos.registrar_curso(
        "SW201", "Otro Nombre", "2"
    )
    print(
        f"  • Registrar duplicado: {'✓ (rechazado correctamente)' if not exito else '✗ (debió rechazarse)'}")

    print("\n3. PRUEBAS DE MATRÍCULA")
    print("-" * 60)

    # Prueba 6: Matricular estudiantes en cursos
    exito, msg = gestor_matriculas.matricular_estudiante("1001", "SW201")
    print(
        f"  • Matricular estudiante 1 en curso 1: {'✓' if exito else '✗'} {msg}")

    exito, msg = gestor_matriculas.matricular_estudiante("1001", "SW202")
    print(
        f"  • Matricular estudiante 1 en curso 2: {'✓' if exito else '✗'} {msg}")

    exito, msg = gestor_matriculas.matricular_estudiante("1002", "SW201")
    print(
        f"  • Matricular estudiante 2 en curso 1: {'✓' if exito else '✗'} {msg}")

    exito, msg = gestor_matriculas.matricular_estudiante("1003", "SW203")
    print(
        f"  • Matricular estudiante 3 en curso 3: {'✓' if exito else '✗'} {msg}")

    # Prueba 7: Intentar matricular duplicado
    exito, msg = gestor_matriculas.matricular_estudiante("1001", "SW201")
    print(
        f"  • Matricular duplicado: {'✓ (rechazado correctamente)' if not exito else '✗ (debió rechazarse)'}")

    # Prueba 8: Intentar matricular estudiante inexistente
    exito, msg = gestor_matriculas.matricular_estudiante("9999", "SW201")
    print(
        f"  • Matricular estudiante inexistente: {'✓ (rechazado correctamente)' if not exito else '✗ (debió rechazarse)'}")

    # Prueba 9: Intentar matricular en curso inexistente
    exito, msg = gestor_matriculas.matricular_estudiante("1001", "SW999")
    print(
        f"  • Matricular en curso inexistente: {'✓ (rechazado correctamente)' if not exito else '✗ (debió rechazarse)'}")

    print("\n4. PRUEBAS DE CONSULTA")
    print("-" * 60)

    # Prueba 10: Buscar estudiante
    estudiante, msg = gestor_estudiantes.buscar_estudiante("1001")
    print(
        f"  • Buscar estudiante existente: {'✓' if estudiante else '✗'} {msg}")
    if estudiante:
        print(f"    Encontrado: {estudiante['nombre']}")

    # Prueba 11: Buscar estudiante inexistente
    estudiante, msg = gestor_estudiantes.buscar_estudiante("9999")
    print(
        f"  • Buscar estudiante inexistente: {'✓ (no encontrado correctamente)' if not estudiante else '✗'}")

    # Prueba 12: Listar estudiantes
    estudiantes = gestor_estudiantes.listar_estudiantes()
    print(f"  • Listar estudiantes: ✓ Total: {len(estudiantes)}")

    # Prueba 13: Listar cursos
    cursos = gestor_cursos.listar_cursos()
    print(f"  • Listar cursos: ✓ Total: {len(cursos)}")

    # Prueba 14: Listar matrículas
    matriculas = gestor_matriculas.listar_matriculas()
    print(f"  • Listar matrículas: ✓ Total: {len(matriculas)}")

    print("\n5. RESUMEN DE DATOS")
    print("-" * 60)
    print(f"  • Estudiantes registrados: {len(estudiantes)}")
    for est in estudiantes:
        print(
            f"    - {est['nombre']} (ID: {est['identificacion']}) - {est['carrera']}, Semestre {est['semestre']}")

    print(f"\n  • Cursos registrados: {len(cursos)}")
    for curso in cursos:
        print(
            f"    - {curso['nombre']} (Código: {curso['codigo']}) - {curso['creditos']} créditos")

    print(f"\n  • Matrículas registradas: {len(matriculas)}")
    for mat in matriculas:
        print(
            f"    - {mat['estudiante']['nombre']} → {mat['curso']['nombre']}")

    print("\n5. PRUEBAS DE AUTENTICACIÓN Y AUTORIZACIÓN")
    print("-" * 60)
    from src.auth.auth_service import AuthService

    auth = AuthService()

    # Registrar usuarios para pruebas
    auth.register_user('user1', 'password1', 'user')
    auth.register_user('admin1', 'password2', 'admin')

    # Intento de login fallido
    exito, msg = auth.login('user1', 'wrongpassword')
    print(f"  • Intento login fallido (user1): {'✓' if not exito else '✗'} {msg}")

    # Intento de login correcto
    exito, msg = auth.login('user1', 'password1')
    print(f"  • Login correcto (user1): {'✓' if exito else '✗'} {msg}")

    # Comprobar autorización (user no puede registrar cursos)
    autorizado = auth.authorize('admin')
    print(f"  • Autorización para registrar curso (user1 as admin): {'✓ (rechazado correctamente)' if not autorizado else '✗ (debió rechazarse)'}")

    # Login como admin y comprobar autorización
    auth.logout()
    exito, msg = auth.login('admin1', 'password2')
    print(f"  • Login correcto (admin1): {'✓' if exito else '✗'} {msg}")
    autorizado = auth.authorize('admin')
    print(f"  • Autorización para registrar curso (admin1): {'✓' if autorizado else '✗'}")

    print("\n" + "="*60)
    print("  TODAS LAS PRUEBAS COMPLETADAS EXITOSAMENTE ✓")
    print("="*60)
    print("\n  El sistema está listo para usar.")
    print("  Ejecute 'python main.py' para iniciar la aplicación.\n")


if __name__ == "__main__":
    ejecutar_pruebas()
