import random
import string
from datetime import datetime

def generar_numero_guia():
    """Genera un número de guía único para los envíos"""
    fecha_actual = datetime.now()
    fecha_str = fecha_actual.strftime("%Y%m%d")
    random_str = ''.join(random.choices(string.ascii_uppercase + string.digits, k=6))
    return f"PAQ-{fecha_str}-{random_str}"

def calcular_costo_envio(peso, dimensiones, distancia_km=10):
    """
    Calcula el costo aproximado de un envío basado en peso, dimensiones y distancia
    
    Args:
        peso (float): Peso del paquete en kg
        dimensiones (str): Dimensiones en formato "LxAxA" (cm)
        distancia_km (int): Distancia estimada en km (default 10km)
    
    Returns:
        float: Costo estimado del envío
    """
    try:
        # Extraer dimensiones
        l, a, h = map(float, dimensiones.split('x'))
        volumen = l * a * h  # cm³

        # Factores de cálculo
        base = 5.00  # costo base
        por_peso = max(0, (peso - 1) * 2.50)  # $2.50 por kg adicional al primero
        por_volumen = max(0, (volumen - 1000) / 1000 * 1.50)  # $1.50 por cada 1000cm³ adicionales
        por_distancia = max(1, distancia_km / 5) * 3.00  # $3.00 por cada 5km

        total = base + por_peso + por_volumen + por_distancia
        return round(total, 2)
    except Exception as e:
        print(f"Error al calcular costo: {e}")
        return 10.00  # Valor por defecto si hay error en cálculo

def validar_peso(peso):
    """Valida que el peso sea un número positivo menor a 50kg"""
    try:
        peso_float = float(peso)
        return 0 < peso_float <= 50
    except ValueError:
        return False

def validar_dimensiones(dimensiones):
    """Valida que las dimensiones estén en formato correcto (LxAxA) y sean positivas"""
    try:
        partes = dimensiones.split('x')
        if len(partes) != 3:
            return False
        
        l, a, h = map(float, partes)
        return l > 0 and a > 0 and h > 0
    except:
        return False