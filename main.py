"""
Sistema Académico - Universidad
Arquitectura en 3 Capas

Autor: Sistema de Gestión Académica
Fecha: 24 de octubre de 2025

Este sistema implementa una arquitectura en 3 capas:
- Capa de Presentación: Interfaz de usuario por terminal
- Capa de Negocio: Lógica de negocio y validaciones
- Capa de Datos: Acceso y almacenamiento de datos

Funcionalidades:
- Registrar estudiantes (nombre, identificación, carrera, semestre)
- Registrar cursos (código, nombre, créditos)
- Matricular estudiantes en cursos
- Listar y consultar información
"""

from src.capa_presentacion.interfaz_terminal import main
import sys
import os

# Agregar el directorio actual al path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))


if __name__ == "__main__":
    main()
