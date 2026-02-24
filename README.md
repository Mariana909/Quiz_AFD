# AFD - Autómata Finito Determinista

Programa que analiza tokens desde un archivo de texto y los clasifica usando un AFD.

## Tokens reconocidos

| Token | Descripción | Ejemplo |
|-------|-------------|---------|
| `SUMA` | El símbolo `+` solo | `+` |
| `INCR` | El símbolo `++` | `++` |
| `ID` | Identificador: mayúscula seguida de mayúsculas, minúsculas o dígitos | `Abc`, `A8b`, `HGU5` |
| `NO ACEPTA` | Cualquier otra cadena | `123`, `+abc` |

## Archivos

```
.
├── AFD.c       # Implementación en C
├── AFD.py      # Implementación en Python
└── entrada.txt # Archivo de tokens de prueba
```

## Compilar y ejecutar (C)

```bash
gcc AFD.c -o AFD
./AFD entrada.txt
```

## Ejecutar (Python)

```bash
python3 AFD.py entrada.txt
```

## Formato del archivo de entrada

El archivo de texto debe tener los tokens separados por espacios o saltos de línea:

```
Asjbco6546
++
+
KOJBjhdkd
```

## Estados del AFD

| Estado | Descripción |
|--------|-------------|
| `q0` | Estado inicial |
| `q1` | SUMA (`+`) |
| `q2` | INCR (`++`) |
| `q3` | ID - solo mayúsculas hasta ahora |
| `q4` | ID - después de una minúscula |
| `q5` | ID - después de un dígito |
| `q6` | Estado de rechazo |
