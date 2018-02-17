import time
import sqlite3
#db=sqlite3.connect(':memory:')

# La base de datos "Toma2.db" se creo  desde DB Browser for SQLite
# Se debe usar la ruta absoluta del archivo de base de dato que contiene la tabla, para poder conectarse
db = sqlite3.connect("C:\Users\Jorge\PycharmProjects\toma2.db")



while True:
    print("  Libros")
    print("  Seleccione uno de las siguientes acciones:")
    Opcion = int(
        input(" 1. Buscar un libro \n 2. Agregar un libro \n3. Eliminar un libro \n Su elección: "))

    cursor = db.cursor()

    # opcion 1  buscar un libro

    if Opcion == 1:
        Isbn = input("\ntPara buscar un libro, favor ingresar su ISBN: ")
        cursor.execute('''SELECT Nombre, Autor FROM Libro WHERE ISBN = ?''', (Isbn,))
        resultado = cursor.fetchall()
        print("\t", resultado, "\n")
        db.commit()
        break

    elif Opcion == 2:
        print("\n\t Introduzca los siguientes datos solicitados: ")
        Isbn = input("\t\tISBN: ")
        Nombre = input("\t\tNombre del libro: ")
        Autor = input("\t\tNombre del autor: ")
        Publicacion = input("\t\tAño de publicacion: ")
        Cantidad_Paginas = input("\t\tCantidad de paginas:")

        cursor.execute('''INSERT INTO Libro(ISBN, Nombre, Autor, Publicacion, Cantidad_Paginas) 
                     VALUES(?,?,?,?,?)''', (Isbn, Nombre, Autor, Publicacion, Cantidad_Paginas))
        db.commit()
        break

    # La Opcion 3 elimina un libro existente utilizando el ISBN como llave.
    elif Opcion == 3:
        ISBN = input("Introduzca el ISBN del libro que quiere eliminar: ")
        cursor.execute('''DELETE FROM Libro WHERE ISBN = ?''', (
            ISBN,))  # Se le pone coma desps de ISBN por que no puede elimaniar sola esa columna debe eliminar todo lo que esta en esa fila. La coma permite incluir todas las columnas restantes sin tener que nombrarlas.
        db.commit()
        break

    print("OPCIÓN EQUIVOCADA. INTENTE NUVEAMENTE")
    time.sleep(1)

db.close()
