# Diagrama de Arquitectura del Sistema Académico

## Estructura extendida con Capa de Autenticación

```
╔═══════════════════════════════════════════════════════════════════════╗
║                       CAPA DE PRESENTACIÓN                            ║
║                    (src/capa_presentacion/)                           ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  ┌─────────────────────────────────────────────────────────────┐    ║
║  │            InterfazUsuario (interfaz_terminal.py)           │    ║
║  │                                                             │    ║
║  │  • mostrar_menu_principal()                                 │    ║
║  │  • menu_estudiantes()                                       │    ║
║  │  • menu_cursos()                                            │    ║
║  │  • menu_matriculas()                                        │    ║
║  │  • registrar_estudiante()                                   │    ║
║  │  • listar_estudiantes()                                     │    ║
║  │  • buscar_estudiante()                                      │    ║
║  │  • registrar_curso() (requiere autorización)                │    ║
║  │  • matricular_estudiante()                                  │    ║
║  └─────────────────────────────────────────────────────────────┘    ║
║                              │                                        ║
║                              │ llama a                                ║
║                              ▼                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
                               │
                               │
╔═══════════════════════════════════════════════════════════════════════╗
║                   CAPA DE AUTENTICACIÓN (nueva)                        ║
║                       (src/auth/)                                       ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  ┌─────────────────────────────────────────────────────────────┐    ║
║  │            AuthService / UserDAO (auth_service.py)          │    ║
║  │                                                             │    ║
║  │  • register_user(username,password,role)                    │    ║
║  │  • login(username,password)                                 │    ║
║  │  • authorize(required_role)                                 │    ║
║  │  • registra intentos fallidos en archivo (auth.log)         │    ║
║  └─────────────────────────────────────────────────────────────┘    ║
║                              │                                        ║
║                              │ valida / controla                     ║
║                              ▼                                        ║
╚═══════════════════════════════════════════════════════════════════════╝
                               │
                               │
╔═══════════════════════════════════════════════════════════════════════╗
║                         CAPA DE NEGOCIO                               ║
║                      (src/capa_negocio/)                              ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  ┌──────────────────┐   ┌──────────────────┐   ┌─────────────────┐  ║
║  │ GestorEstudiantes│   │   GestorCursos   │   │GestorMatriculas │  ║
║  │                  │   │                  │   │                 │  ║
║  │ • registrar()    │   │ • registrar()    │   │ • matricular()  │  ║
║  │ • buscar()       │   │ • buscar()       │   │ • listar()      │  ║
║  │ • listar()       │   │ • listar()       │   │                 │  ║
║  │ • validaciones   │   │ • validaciones   │   │ • validaciones  │  ║
║  └────────┬─────────┘   └────────┬─────────┘   └────────┬────────┘  ║
║           │                      │                       │           ║
║           │ usa                  │ usa                   │ usa       ║
║           ▼                      ▼                       ▼           ║
╚═══════════════════════════════════════════════════════════════════════╝
           │                      │                       │
           │                      │                       │
╔═══════════════════════════════════════════════════════════════════════╗
║                          CAPA DE DATOS                                ║
║                       (src/capa_datos/)                               ║
╠═══════════════════════════════════════════════════════════════════════╣
║                                                                       ║
║  ┌──────────────────┐   ┌──────────────────┐   ┌─────────────────┐  ║
║  │ EstudianteDAO    │   │    CursoDAO      │   │  MatriculaDAO   │  ║
║  │                  │   │                  │   │                 │  ║
║  │ • guardar()      │   │ • guardar()      │   │ • guardar()     │  ║
║  │ • buscar_por_id()│   │ • buscar_por_cod │   │ • existe_mat()  │  ║
║  │ • listar_todos() │   │ • listar_todos() │   │ • listar_todas()│  ║
║  │ • existe()       │   │ • existe()       │   │ • buscar()      │  ║
║  └────────┬─────────┘   └────────┬─────────┘   └────────┬────────┘  ║
║           │                      │                       │           ║
║           ▼                      ▼                       ▼           ║
║  ┌─────────────────────────────────────────────────────────────┐    ║
║  │             Almacenamiento en Memoria (listas)              │    ║
║  │  • estudiantes[]    • cursos[]    • matriculas[]            │    ║
║  └─────────────────────────────────────────────────────────────┘    ║
║                                                                       ║
╚═══════════════════════════════════════════════════════════════════════╝
```

## Flujo de Datos (Ejemplo: Registrar Estudiante)

```
1. USUARIO
   └─> Ingresa datos en terminal

2. CAPA DE PRESENTACIÓN
   └─> InterfazUsuario.registrar_estudiante()
       • Captura: nombre, identificación, carrera, semestre
       • Llama a: gestor_estudiantes.registrar_estudiante()

3. CAPA DE NEGOCIO
   └─> GestorEstudiantes.registrar_estudiante()
       • Valida que nombre no esté vacío
       • Valida que identificación sea única
       • Valida que semestre sea número positivo
       • Llama a: estudiante_dao.existe()
       • Llama a: estudiante_dao.guardar()

4. CAPA DE DATOS
   └─> EstudianteDAO.guardar()
       • Agrega estudiante a la lista estudiantes[]
       • Retorna: True

5. RETORNO
   └─> Negocio: Retorna (True, "Estudiante registrado exitosamente")
       └─> Presentación: Muestra mensaje de éxito al usuario
           └─> Usuario: Ve confirmación en pantalla
```

## Modelo de Datos

```
┌─────────────────────┐
│    ESTUDIANTE       │
├─────────────────────┤
│ - nombre: str       │
│ - identificacion:str│ (PK)
│ - carrera: str      │
│ - semestre: int     │
└──────────┬──────────┘
           │
           │ N
           │
           ▼ N
┌─────────────────────┐
│    MATRÍCULA        │
├─────────────────────┤
│ - id_estudiante:str │ (FK)
│ - codigo_curso: str │ (FK)
└──────────┬──────────┘
           │
           │ N
           │
           ▼ 1
┌─────────────────────┐
│      CURSO          │
├─────────────────────┤
│ - codigo: str       │ (PK)
│ - nombre: str       │
│ - creditos: int     │
└─────────────────────┘
```

## Principios de Diseño Aplicados

### 1. Separación de Responsabilidades (SoC)

- Cada capa tiene una responsabilidad única y bien definida
- No hay mezcla de lógica de presentación con lógica de negocio

### 2. Dependencias Unidireccionales

- Presentación → Negocio → Datos
- Una capa superior puede llamar a una inferior
- Una capa inferior NUNCA llama a una superior

### 3. Bajo Acoplamiento

- Las capas se comunican mediante interfaces claras
- Cambios en una capa no afectan a las otras (si se mantiene la interfaz)

### 4. Alta Cohesión

- Cada módulo agrupa funcionalidades relacionadas
- DAOs solo manejan datos
- Gestores solo manejan lógica de negocio
- Interfaz solo maneja presentación

### 5. Patrón DAO (Data Access Object)

- Abstracción del acceso a datos
- Facilita cambiar la implementación de almacenamiento
- Operaciones CRUD centralizadas

## Ventajas de esta Arquitectura

✅ **Mantenibilidad**: Fácil de modificar y corregir
✅ **Testabilidad**: Cada capa se puede probar independientemente
✅ **Escalabilidad**: Se puede reemplazar una capa sin afectar las demás
✅ **Reutilización**: La lógica de negocio sirve para diferentes interfaces
✅ **Claridad**: El código es fácil de entender y seguir

## Posibles Extensiones Futuras

1. **Capa de Datos**:

   - Agregar persistencia en base de datos (SQLite, PostgreSQL)
   - Implementar almacenamiento en archivos JSON/CSV

2. **Capa de Negocio**:

   - Agregar más validaciones (cupo máximo de estudiantes)
   - Implementar prerrequisitos de cursos
   - Calcular promedio de notas

3. **Capa de Presentación**:
   - Agregar interfaz gráfica (Tkinter, PyQt)
   - Crear API REST (Flask, FastAPI)
   - Desarrollar interfaz web (Django)
