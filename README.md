# Sistema Académico - Arquitectura en 3 Capas

## 📋 Descripción

Sistema de gestión académica desarrollado en Python con arquitectura de 3 capas para la gestión de estudiantes, cursos y matrículas. Este proyecto implementa una separación clara de responsabilidades siguiendo los principios de arquitectura de software limpia y modular.

## 🏗️ Arquitectura del Sistema

El sistema está estructurado en tres capas principales que garantizan claridad, mantenibilidad y modularidad:

### 1. **Capa de Presentación** (`src/capa_presentacion/`)

- **Responsabilidad**: Interactuar con el usuario a través de la terminal
- **Características**:
  - Menús interactivos por consola
  - Captura de datos de entrada
  - Visualización de resultados
  - No contiene lógica de negocio
- **Archivo principal**: `interfaz_terminal.py`

### 2. **Capa de Negocio** (`src/capa_negocio/`)

- **Responsabilidad**: Implementar reglas de negocio y validaciones
- **Características**:
  - Validación de datos de entrada
  - Prevención de duplicados
  - Control de reglas de matrícula
  - Coordinación entre capas
- **Componentes**:
  - `gestor_estudiantes.py`: Lógica de estudiantes
  - `gestor_cursos.py`: Lógica de cursos
  - `gestor_matriculas.py`: Lógica de matrículas

### 3. **Capa de Datos** (`src/capa_datos/`)

- **Responsabilidad**: Gestionar el almacenamiento de información
- **Características**:
  - Operaciones CRUD básicas
  - Almacenamiento en memoria (no persistente)
  - Acceso a datos mediante DAOs (Data Access Objects)
- **Componentes**:
  - `estudiante_dao.py`: Acceso a datos de estudiantes
  - `curso_dao.py`: Acceso a datos de cursos
  - `matricula_dao.py`: Acceso a datos de matrículas

## 📁 Estructura del Proyecto

```
Taller_arquitectura_capas/
│
├── src/
│   ├── __init__.py
│   │
│   ├── capa_datos/
│   │   ├── __init__.py
│   │   ├── estudiante_dao.py      # DAO de estudiantes
│   │   ├── curso_dao.py            # DAO de cursos
│   │   └── matricula_dao.py        # DAO de matrículas
│   │
│   ├── capa_negocio/
│   │   ├── __init__.py
│   │   ├── gestor_estudiantes.py  # Lógica de negocio de estudiantes
│   │   ├── gestor_cursos.py        # Lógica de negocio de cursos
│   │   └── gestor_matriculas.py    # Lógica de negocio de matrículas
│   │
│   └── capa_presentacion/
│       ├── __init__.py
│       └── interfaz_terminal.py    # Interfaz de usuario por terminal
│
├── main.py                         # Punto de entrada de la aplicación
├── pruebas.py                      # Script de pruebas básicas
└── README.md                       # Este archivo
```

## 🎯 Requisitos Funcionales

El sistema permite:

- ✅ **Registrar estudiantes** con los siguientes datos:

  - Nombre completo
  - Identificación única
  - Carrera
  - Semestre actual

- ✅ **Registrar cursos** con:

  - Código único
  - Nombre del curso
  - Número de créditos

- ✅ **Matricular estudiantes** en cursos con validaciones:

  - Verificación de existencia de estudiante y curso
  - Prevención de matrículas duplicadas

- ✅ **Listar información**:

  - Todos los estudiantes registrados
  - Todos los cursos disponibles
  - Todas las matrículas realizadas

- ✅ **Buscar estudiante** por identificación

## 🔧 Requisitos No Funcionales

- **Mantenibilidad**: Código modularizado por capas con responsabilidades únicas
- **Claridad**: Cada capa cumple una función específica y bien definida
- **Reutilización**: Las funciones de negocio pueden ser llamadas desde diferentes interfaces
- **Modularidad**: Dependencias unidireccionales (Presentación → Negocio → Datos)

## 🚀 Instalación y Ejecución

### Prerrequisitos

- Python 3.6 o superior

### Pasos para ejecutar

1. **Clonar o descargar el proyecto**

2. **Navegar al directorio del proyecto**

   ```powershell
   cd "H:\Mi unidad\Documentos\Trabajos-UPTC\Semestre-9\Software2\Taller_arquitectura_capas"
   ```

3. **Ejecutar las pruebas básicas** (opcional pero recomendado)

   ```powershell
   python pruebas.py
   ```

4. **Ejecutar la aplicación principal**
   ```powershell
   python main.py
   ```

## 📖 Guía de Uso

### Menú Principal

Al ejecutar la aplicación, verás el siguiente menú:

```
==================================================
    SISTEMA ACADÉMICO - GESTIÓN UNIVERSITARIA
==================================================

1. Gestión de Estudiantes
2. Gestión de Cursos
3. Gestión de Matrículas
4. Consultas y Listados
0. Salir
```

### Flujo de Uso Recomendado

1. **Registrar Estudiantes**: Opción 1 → Opción 1
2. **Registrar Cursos**: Opción 2 → Opción 1
3. **Matricular Estudiantes**: Opción 3 → Opción 1
4. **Consultar Información**: Opción 4

## 🧪 Pruebas

El archivo `pruebas.py` ejecuta un conjunto completo de pruebas que verifican:

- ✓ Registro de estudiantes con validaciones
- ✓ Registro de cursos con validaciones
- ✓ Proceso de matrícula con validaciones
- ✓ Prevención de duplicados
- ✓ Búsqueda de información
- ✓ Listado de todos los elementos
- ✓ Manejo de errores y casos límite

### Ejecutar pruebas

```powershell
python pruebas.py
```

## 🔄 Flujo de Dependencias

```
┌─────────────────────────┐
│  Capa de Presentación   │
│   (interfaz_terminal)   │
└───────────┬─────────────┘
            │ llama a
            ▼
┌─────────────────────────┐
│   Capa de Negocio       │
│  (gestores + validación)│
└───────────┬─────────────┘
            │ llama a
            ▼
┌─────────────────────────┐
│    Capa de Datos        │
│  (DAOs + almacenamiento)│
└─────────────────────────┘
```

**Principio fundamental**: Las dependencias fluyen solo de forma descendente.

## 💡 Validaciones Implementadas

### Estudiantes

- Nombre no puede estar vacío
- Identificación no puede estar vacía
- No se permiten identificaciones duplicadas
- Carrera no puede estar vacía
- Semestre debe ser un número positivo

### Cursos

- Código no puede estar vacío
- No se permiten códigos duplicados
- Nombre no puede estar vacío
- Créditos deben ser un número positivo

### Matrículas

- El estudiante debe existir previamente
- El curso debe existir previamente
- No se permite matricular dos veces en el mismo curso
- Identificación y código no pueden estar vacíos

## 📝 Ejemplos de Uso

### Ejemplo 1: Registrar un Estudiante

```
Nombre completo: Juan Pérez García
Identificación: 1001
Carrera: Ingeniería de Sistemas
Semestre: 5

✓ Estudiante registrado exitosamente
```

### Ejemplo 2: Registrar un Curso

```
Código del curso: SW201
Nombre del curso: Programación Orientada a Objetos
Número de créditos: 4

✓ Curso registrado exitosamente
```

### Ejemplo 3: Matricular un Estudiante

```
Identificación del estudiante: 1001
Código del curso: SW201

✓ Matrícula realizada exitosamente
```

## 🛠️ Tecnologías Utilizadas

- **Lenguaje**: Python 3
- **Paradigma**: Programación Orientada a Objetos
- **Patrón de Arquitectura**: Arquitectura en 3 Capas
- **Patrón de Diseño**: DAO (Data Access Object)

---

**Nota**: Este sistema utiliza almacenamiento en memoria, por lo que los datos se pierden al cerrar la aplicación. 
