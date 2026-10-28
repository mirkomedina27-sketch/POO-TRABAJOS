# ==============================================================================
# 1. CLASE BASE CON LA REGLA INSTITUCIONAL ÚNICA
# ==============================================================================

class MatriculaGeneral:
    def calcular_desglose(self) -> dict:
        # Hara una bolsa de datos
        return {
            "base": 60.0,
            "recargos": 0.0,
            "descuento_beca": 0.0
        }

    def calcular_monto(self) -> float:
        """
        Regla que se usará:
        1. Se suman todos los recargos acumulados al derecho base.
        2. La beca se aplica estrictamente al final sobre el subtotal obtenido.
        """
        desglose = self.calcular_desglose()
        subtotal = desglose["base"] + desglose["recargos"]
        total_final = subtotal * (1.0 - desglose["descuento_beca"])
        return total_final


# ==============================================================================
# 2. CLASES HIJAS: SOLO REGISTRAN DATOS (NO OPERAN NÚMEROS A CIEGAS)
# ==============================================================================

class MatriculaExtemporanea(MatriculaGeneral):
    def calcular_desglose(self) -> dict:
        datos = super().calcular_desglose()
        datos["recargos"] += 15.0
        return datos


class MatriculaDesaprobatoria(MatriculaGeneral):
    def calcular_desglose(self) -> dict:
        datos = super().calcular_desglose()
        datos["recargos"] += 15.0
        return datos


class MatriculaBeca(MatriculaGeneral):
    def calcular_desglose(self) -> dict:
        datos = super().calcular_desglose()
        datos["descuento_beca"] = 0.50
        return datos


# ==============================================================================
# 3. CLASES COMBINADAS (HERENCIA MÚLTIPLE EN DISTINTO ORDEN)
# ==============================================================================

# Programador 1 escribió Beca primero:
class MatriculaCombinadaProg1(MatriculaBeca, MatriculaDesaprobatoria, MatriculaExtemporanea):
    pass


# Programador 2 escribió Beca al final:
class MatriculaCombinadaProg2(MatriculaDesaprobatoria, MatriculaExtemporanea, MatriculaBeca):
    pass


# ==============================================================================
# 4. COMPROBACIÓN: EQUIDAD TOTAL EN EL COBRO
# ==============================================================================

print("=" * 75)
print("SISTEMA DE MATRÍCULA UNSCH - REGLA: BECA APLICADA AL FINAL")
print("=" * 75)

# Instanciación y llamada directa en una sola línea sin variables intermedias:
print(f"Cobro Luis: S/ {MatriculaCombinadaProg1().calcular_monto():.2f}")
print(f"Cobro Rosa: S/ {MatriculaCombinadaProg2().calcular_monto():.2f}")



