# Pedir el nombre del producto esto es un texto que el usuario ingresa
nombre_producto = input("Ingrese el nombre del producto: ")   

#Pedir el precio del producto esto es un numero entero o decimal
while True: #un bucle para repetir la pregunta
    try:
        precio_unitario = float(input("Ingrese el precio del producto: "))
        break  # Salir del bucle si la conversión es exitosa
    except ValueError:
        # excep se activa si el usuario escribe letras y el try falla
        print("Error por favor ingrese un número válido para el precio.")    

#Pedir la cantidad. Debe ser un número entero ('int')
#usamos otro bucle para validar la cantidad
while True:
    try:
        cantidad = int(input("Ingrese la cantidad del producto: "))
        break  # Si funciona, 'break' rompe el bucle y salimos
    except ValueError:
        # excep se activa si el usuario escribe letras y el try falla
        print("Error La cantidad debe ser un número entero. Intente de nuevo.")    
# multiplicamos el preciio y la cantidad 
costo_total = precio_unitario * cantidad
# Mostramos un resumen usando un 'f-string' (la f antes de las comillas)     
print("\n--- RESUMEN DEL PRODUCTO ---")
print(f"Producto: {nombre_producto} | Precio: ${precio_unitario} | Cantidad: {cantidad} | Total: ${costo_total}")
#Este programa registra un producto que valida el precio y a cantidad
# y calcula el costo total del inventario