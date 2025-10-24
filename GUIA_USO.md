# Guía de Uso Detallada - Sistema Académico

## 🚀 Inicio Rápido

### Paso 1: Ejecutar las Pruebas

```powershell
python pruebas.py
```

Este comando ejecutará un conjunto completo de pruebas automáticas que verifican todas las funcionalidades del sistema.

### Paso 2: Ejecutar la Aplicación

```powershell
python main.py
```

## 📖 Tutorial Paso a Paso

### Escenario de Uso Completo

Vamos a simular el registro de una universidad con estudiantes, cursos y matrículas.

---

## 1️⃣ Registrar Estudiantes

**Opción del menú**: `1` → `1`

### Ejemplo 1: Estudiante de Ingeniería de Sistemas

```
Nombre completo: Ana María García López
Identificación: 202310001
Carrera: Ingeniería de Sistemas
Semestre: 5

✓ Estudiante registrado exitosamente
```

### Ejemplo 2: Estudiante de Ingeniería Industrial

```
Nombre completo: Carlos Eduardo Martínez
Identificación: 202310002
Carrera: Ingeniería Industrial
Semestre: 3

✓ Estudiante registrado exitosamente
```

### Ejemplo 3: Estudiante de Arquitectura

```
Nombre completo: Laura Sofía Rodríguez
Identificación: 202310003
Carrera: Arquitectura
Semestre: 7

✓ Estudiante registrado exitosamente
```

### ❌ Ejemplo de Error: Identificación Duplicada

```
Nombre completo: Pedro González
Identificación: 202310001
Carrera: Ingeniería Civil
Semestre: 2

❌ Error: Ya existe un estudiante con la identificación 202310001
```

---

## 2️⃣ Registrar Cursos

**Opción del menú**: `2` → `1`

### Ejemplo 1: Curso de Programación

```
Código del curso: SW301
Nombre del curso: Programación Orientada a Objetos
Número de créditos: 4

✓ Curso registrado exitosamente
```

### Ejemplo 2: Curso de Bases de Datos

```
Código del curso: SW302
Nombre del curso: Bases de Datos Relacionales
Número de créditos: 3

✓ Curso registrado exitosamente
```

### Ejemplo 3: Curso de Arquitectura

```
Código del curso: SW401
Nombre del curso: Arquitectura de Software
Número de créditos: 4

✓ Curso registrado exitosamente
```

### Ejemplo 4: Curso de Redes

```
Código del curso: SW303
Nombre del curso: Redes de Computadores
Número de créditos: 3

✓ Curso registrado exitosamente
```

### ❌ Ejemplo de Error: Código Duplicado

```
Código del curso: SW301
Nombre del curso: Otro curso
Número de créditos: 2

❌ Error: Ya existe un curso con el código SW301
```

---

## 3️⃣ Buscar Estudiante

**Opción del menú**: `1` → `2`

### Búsqueda Exitosa

```
Identificación del estudiante: 202310001

✓ Estudiante encontrado

----------------------------------------------------
Nombre:         Ana María García López
Identificación: 202310001
Carrera:        Ingeniería de Sistemas
Semestre:       5
----------------------------------------------------
```

### ❌ Estudiante No Encontrado

```
Identificación del estudiante: 999999

❌ No se encontró estudiante con identificación 999999
```

---

## 4️⃣ Listar Todos los Estudiantes

**Opción del menú**: `1` → `3` o `4` → `1`

### Salida Esperada

```
----------------------------------------------------
    LISTADO DE ESTUDIANTES
----------------------------------------------------

Total de estudiantes: 3

1. Ana María García López
   ID: 202310001 | Carrera: Ingeniería de Sistemas | Semestre: 5

2. Carlos Eduardo Martínez
   ID: 202310002 | Carrera: Ingeniería Industrial | Semestre: 3

3. Laura Sofía Rodríguez
   ID: 202310003 | Carrera: Arquitectura | Semestre: 7
```

---

## 5️⃣ Buscar Curso

**Opción del menú**: `2` → `2`

### Búsqueda Exitosa

```
Código del curso: SW301

✓ Curso encontrado

----------------------------------------------------
Código:   SW301
Nombre:   Programación Orientada a Objetos
Créditos: 4
----------------------------------------------------
```

---

## 6️⃣ Listar Todos los Cursos

**Opción del menú**: `2` → `3` o `4` → `2`

### Salida Esperada

```
----------------------------------------------------
    LISTADO DE CURSOS
----------------------------------------------------

Total de cursos: 4

1. Programación Orientada a Objetos
   Código: SW301 | Créditos: 4

2. Bases de Datos Relacionales
   Código: SW302 | Créditos: 3

3. Arquitectura de Software
   Código: SW401 | Créditos: 4

4. Redes de Computadores
   Código: SW303 | Créditos: 3
```

---

## 7️⃣ Matricular Estudiantes en Cursos

**Opción del menú**: `3` → `1`

### Ejemplo 1: Matrícula Exitosa

```
Identificación del estudiante: 202310001
Código del curso: SW301

✓ Matrícula realizada exitosamente
```

### Ejemplo 2: Múltiples Matrículas para un Estudiante

```
# Ana María se matricula en varios cursos
Identificación: 202310001, Curso: SW302 → ✓
Identificación: 202310001, Curso: SW401 → ✓
Identificación: 202310001, Curso: SW303 → ✓
```

### Ejemplo 3: Varios Estudiantes en un Curso

```
# Varios estudiantes se matriculan en POO
Identificación: 202310002, Curso: SW301 → ✓
Identificación: 202310003, Curso: SW301 → ✓
```

### ❌ Ejemplo de Error: Matrícula Duplicada

```
Identificación del estudiante: 202310001
Código del curso: SW301

❌ Error: El estudiante ya está matriculado en el curso SW301
```

### ❌ Ejemplo de Error: Estudiante No Existe

```
Identificación del estudiante: 999999
Código del curso: SW301

❌ Error: No existe estudiante con identificación 999999
```

### ❌ Ejemplo de Error: Curso No Existe

```
Identificación del estudiante: 202310001
Código del curso: SW999

❌ Error: No existe curso con código SW999
```

---

## 8️⃣ Listar Todas las Matrículas

**Opción del menú**: `3` → `2` o `4` → `3`

### Salida Esperada

```
----------------------------------------------------
    LISTADO DE MATRÍCULAS
----------------------------------------------------

Total de matrículas: 6

1. Estudiante: Ana María García López (ID: 202310001)
   Curso: Programación Orientada a Objetos (Código: SW301) - 4 créditos

2. Estudiante: Ana María García López (ID: 202310001)
   Curso: Bases de Datos Relacionales (Código: SW302) - 3 créditos

3. Estudiante: Ana María García López (ID: 202310001)
   Curso: Arquitectura de Software (Código: SW401) - 4 créditos

4. Estudiante: Ana María García López (ID: 202310001)
   Curso: Redes de Computadores (Código: SW303) - 3 créditos

5. Estudiante: Carlos Eduardo Martínez (ID: 202310002)
   Curso: Programación Orientada a Objetos (Código: SW301) - 4 créditos

6. Estudiante: Laura Sofía Rodríguez (ID: 202310003)
   Curso: Programación Orientada a Objetos (Código: SW301) - 4 créditos
```

---

## 🔍 Casos de Validación

### Validaciones de Estudiante

#### ❌ Nombre Vacío

```
Nombre completo:
Identificación: 202310004
Carrera: Ingeniería
Semestre: 1

❌ Error: El nombre no puede estar vacío
```

#### ❌ Identificación Vacía

```
Nombre completo: Juan Pérez
Identificación:
Carrera: Ingeniería
Semestre: 1

❌ Error: La identificación no puede estar vacía
```

#### ❌ Carrera Vacía

```
Nombre completo: Juan Pérez
Identificación: 202310004
Carrera:
Semestre: 1

❌ Error: La carrera no puede estar vacía
```

#### ❌ Semestre Inválido

```
Nombre completo: Juan Pérez
Identificación: 202310004
Carrera: Ingeniería
Semestre: abc

❌ Error: El semestre debe ser un número válido
```

#### ❌ Semestre Negativo

```
Nombre completo: Juan Pérez
Identificación: 202310004
Carrera: Ingeniería
Semestre: -1

❌ Error: El semestre debe ser un número positivo
```

### Validaciones de Curso

#### ❌ Código Vacío

```
Código del curso:
Nombre del curso: Curso de Prueba
Número de créditos: 3

❌ Error: El código no puede estar vacío
```

#### ❌ Nombre Vacío

```
Código del curso: SW999
Nombre del curso:
Número de créditos: 3

❌ Error: El nombre no puede estar vacío
```

#### ❌ Créditos Inválidos

```
Código del curso: SW999
Nombre del curso: Curso de Prueba
Número de créditos: abc

❌ Error: Los créditos deben ser un número válido
```

---

## 💡 Consejos de Uso

### 1. Orden Recomendado de Operaciones

1. **Primero**: Registrar estudiantes
2. **Segundo**: Registrar cursos
3. **Tercero**: Matricular estudiantes en cursos
4. **Finalmente**: Consultar y listar información

### 2. Códigos de Identificación

- Use códigos únicos y fáciles de recordar
- Para estudiantes: Año + número secuencial (ej: 202310001)
- Para cursos: Prefijo de facultad + número (ej: SW301)

### 3. Navegación en los Menús

- Use números para seleccionar opciones
- Use `0` para volver al menú anterior
- Presione Enter para continuar después de cada operación

### 4. Validaciones Automáticas

El sistema valida automáticamente:

- ✅ Unicidad de identificaciones y códigos
- ✅ Campos no vacíos
- ✅ Tipos de datos correctos
- ✅ Existencia de estudiantes y cursos al matricular

---

## 🎓 Caso de Uso Completo: Semestre Académico

### Escenario

Una universidad necesita registrar la información de 3 estudiantes que se matricularán en cursos del programa de Ingeniería de Sistemas.

### Paso 1: Registrar Estudiantes (Menú 1 → 1)

```
1. Juan Pérez (202310001) - Ingeniería de Sistemas - Semestre 5
2. María López (202310002) - Ingeniería de Sistemas - Semestre 5
3. Carlos Gómez (202310003) - Ingeniería de Sistemas - Semestre 3
```

### Paso 2: Registrar Cursos (Menú 2 → 1)

```
1. SW301 - Programación Orientada a Objetos - 4 créditos
2. SW302 - Bases de Datos - 3 créditos
3. SW303 - Arquitectura de Software - 4 créditos
4. SW101 - Introducción a la Programación - 3 créditos
```

### Paso 3: Matricular Estudiantes (Menú 3 → 1)

```
# Estudiante 1 (Semestre 5 - cursos avanzados)
Juan (202310001) → SW301, SW302, SW303

# Estudiante 2 (Semestre 5 - cursos avanzados)
María (202310002) → SW301, SW302, SW303

# Estudiante 3 (Semestre 3 - curso básico)
Carlos (202310003) → SW101
```

### Paso 4: Verificar Matrículas (Menú 3 → 2)

```
Total de matrículas: 7
- 3 matrículas para Juan
- 3 matrículas para María
- 1 matrícula para Carlos
```

---

## 🔧 Solución de Problemas

### Problema: "Ya existe un estudiante/curso"

**Solución**: Use la opción de buscar para verificar los datos existentes antes de intentar registrar duplicados.

### Problema: "No existe estudiante/curso"

**Solución**: Primero registre el estudiante o curso, luego intente la matrícula.

### Problema: El sistema no guarda los datos

**Nota**: Este sistema usa almacenamiento en memoria. Los datos se pierden al cerrar la aplicación. Esto es intencional para esta versión.

---

## 📊 Estadísticas de Ejemplo

Después de un uso típico:

- **Estudiantes**: 10-20 registrados
- **Cursos**: 15-30 registrados
- **Matrículas**: 40-100 registradas
- **Créditos por estudiante**: 12-18 promedio

---

¡Disfruta usando el Sistema Académico! 🎓
