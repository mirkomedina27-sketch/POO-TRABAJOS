# ==============================================================================
# DEFINICIÓN DE CLASES
# ==============================================================================

class MatriculaGeneral:
    def calcular_monto(self) -> float:
        base = 60.0
        print(f"MatriculaGeneral fija la base en: S/ {base:.2f}")
        return base


class MatriculaExtemporanea(MatriculaGeneral):
    """Suma S/ 15.00 de recargo."""
    def calcular_monto(self) -> float:
        monto_recibido = super().calcular_monto()
        resultado = monto_recibido + 15.0
        print(f"Extemporanea recibe S/ {monto_recibido:.2f} + 15.00  = S/ {resultado:.2f}")
        return resultado


class MatriculaDesaprobatoria(MatriculaGeneral):
    def calcular_monto(self) -> float:
        monto_recibido = super().calcular_monto()
        resultado = monto_recibido + 15.0
        print(f"Desaprobatoria recibe S/ {monto_recibido:.2f} + 15.00 = S/ {resultado:.2f}")
        return resultado


class MatriculaBeca(MatriculaGeneral):
    def calcular_monto(self) -> float:
        monto_recibido = super().calcular_monto()
        resultado = monto_recibido * 0.50
        print(f"Beca recibe S/ {monto_recibido:.2f} x 0.50 (mitad)  = S/ {resultado:.2f}")
        return resultado


# ==============================================================================
# CLASES COMBINADAS (HERENCIA MÚLTIPLE)
# ==============================================================================

# Programador 1 
class MatriculaCombinadaProg1(MatriculaBeca, MatriculaDesaprobatoria, MatriculaExtemporanea):
    pass


# Programador 2 
class MatriculaCombinadaProg2(MatriculaDesaprobatoria, MatriculaExtemporanea, MatriculaBeca):
    pass


# ==============================================================================
# MRO Y EJECUCIÓN PASO A PASO
# ==============================================================================

print("=" * 80)
print("MRO Y LLAMADAS PARA EL CÁLCULO")
print("=" * 80)

print("\n--- LUIS HUAMANÍ (Versión Programador 1) ---")
print("Orden MRO de búsqueda:")
print("  " + " -> ".join([c.__name__ for c in MatriculaCombinadaProg1.__mro__]))
print("Ejecución paso a paso:")
luis = MatriculaCombinadaProg1()
monto_luis = luis.calcular_monto()
print(f">> TOTAL COBRADO A LUIS: S/ {monto_luis:.2f}")

print("\n--- ROSA CCAHUANA (Versión Programador 2) ---")
print("Orden MRO de búsqueda:")
print("  " + " -> ".join([c.__name__ for c in MatriculaCombinadaProg2.__mro__]))
print("Ejecución paso a paso:")
rosa = MatriculaCombinadaProg2()
monto_rosa = rosa.calcular_monto()
print(f">> TOTAL COBRADO A ROSA: S/ {monto_rosa:.2f}")


# ==============================================================================
# PPROBLEMA COBRO DIFERENTE
# ==============================================================================
print("\n" + "=" * 80)
print("EXPLICACIÓN DE LA CAUSA")
print("=" * 80)
print(f"""
¿Por qué cobró distinto?
- A Luis la Beca le tocó al final: (60 base + 15 + 15) x 0.5 = S/ {monto_luis:.2f}
- A Rosa la Beca le tocó al inicio: (60 base x 0.5) + 15 + 15 = S/ {monto_rosa:.2f}

¿Por qué no hubo error de sintaxis?
Porque en Python escribir `class Hijo(A, B, C):` es admitido debido a que nunca
se puso era regla o reestricción.

""")


# ==============================================================================
# ERROR SI SE ESCRIBE LA CLASE GENERAL PRIMERO
# ==============================================================================
print("=" * 80)
print("¿QUÉ PASA SI SE PONE LA GENERAL ANTES DE UNA HIJA?")
print("=" * 80)

try:
    type("MatriculaInvalida", (MatriculaGeneral, MatriculaExtemporanea), {})
except TypeError as error:
    print(f"Python bloquea la creación inmediatamente con un error:\n  -> {error}")
    print("Motivo: El padre (General) no puede resolverse antes que su propio hijo (Extemporanea).")
