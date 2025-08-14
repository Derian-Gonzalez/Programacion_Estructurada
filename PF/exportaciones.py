import pandas as pd
from clientes import obtener_clientes
from envios import obtener_envios

def exportar_clientes_excel():
    """Exporta la lista de clientes a un archivo Excel"""
    clientes = obtener_clientes()
    if not clientes:
        print("No hay clientes para exportar.")
        return
    
    df = pd.DataFrame(clientes)
    archivo = "clientes_exportados.xlsx"
    df.to_excel(archivo, index=False)
    print(f"Clientes exportados correctamente a {archivo}")

def exportar_envios_excel():
    """Exporta la lista de envíos a un archivo Excel"""
    envios = obtener_envios()
    if not envios:
        print("No hay envíos para exportar.")
        return
    
    df = pd.DataFrame(envios)
    archivo = "envios_e-xportados.xlsx"
    df.to_excel(archivo, index=False)
    print(f"Envíos exportados correctamente a {archivo}")
if __name__ == "__main__":
    exportar_clientes_excel()
    exportar_envios_excel()
