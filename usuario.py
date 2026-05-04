from ejercicio_descarte import LinkedList
lista = LinkedList()
start = 1

while start != 0:
        print("""Seleccione la opcion que desee realizar:
    1. Insertar dato al inicio
    2. Mostrar lista 
    3. Descarte
    4. Salir
    """)
    
        o = int(input("Opción: "))

        match o:
            case 1:
                data = float(input("Ingrese el dato que desee insertar al inicio: "))
                lista.insert_at_end(data)
                print("Se inserto el dato correctamente.")
            case 2: 
                lista.display()
            case 3:
                k = int(input("¿Cuál quiere que sea su k?"))
                lista.eliminar_descarte(k)
            case 4:
                  lista.zigzag()
            case 5:
                o = 4
                start = 0