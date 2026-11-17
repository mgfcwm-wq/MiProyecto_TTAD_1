#################################################
# AUTOR: Martin Gomez Fernandez
# FECHA: 18/11/2026
# PROBLEMA
# Implementa en analsis.py las siguientes funcionalidades:
# 1. total facturado
# 2. ventas por categoria
# 3. producto más vendido
#################################################

import json

# NOTA: He utilizado path completo de la ruta para abrir el archivo. 
# Si lo ejecutas en otro equipo, asegúrate de cambiarlo a la ruta correcta donde tengas el archivo data.json.
with open('C:/Proyectos/Proyecto_TTAD_1/Proyecto_TTAD_1/data.json', 'r', encoding='utf-8') as archivo:
  datos = json.load(archivo)

# 1. total facturado sumando (cantidad * precio_unitario) de cada venta
total_facturado = sum(
    venta['cantidad'] * venta['precio_unitario'] 
    for venta in datos['ventas']
)
print(f"1. Total facturado: {total_facturado:.2f} €")

# 2. ventas por categoria
ventas_por_categoria = {}

for venta in datos['ventas']:
    categoria = venta['categoria']
    subtotal = venta['cantidad'] * venta['precio_unitario']
    ventas_por_categoria[categoria] = (
        ventas_por_categoria.get(categoria, 0.0) + subtotal
    )
print("\n2. Ventas por categoría:")
for categoria, total in ventas_por_categoria.items():
    print(f'{categoria}: {total:.2f} €')

# 3. producto más vendido
unidades_por_producto = {}

for venta in datos['ventas']:
    producto = venta['producto']
    cantidad = venta['cantidad']
    unidades_por_producto[producto] = (
        unidades_por_producto.get(producto, 0) + cantidad
    )

# Obtener el producto con mayor cantidad de unidades vendidas
producto_mas_vendido = max(
    unidades_por_producto, key=unidades_por_producto.get
)
total_unidades = unidades_por_producto[producto_mas_vendido]

print(f'\n3.Producto más vendido: {producto_mas_vendido} ({total_unidades} unidades)')