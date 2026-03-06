from servicios.biblioteca_servicio import BibliotecaServicio


def mostrar_menu():

    print("\n===== SISTEMA BIBLIOTECA =====")
    print("1. Añadir libro")
    print("2. Quitar libro")
    print("3. Registrar usuario")
    print("4. Eliminar usuario")
    print("5. Prestar libro")
    print("6. Devolver libro")
    print("7. Buscar libro por título")
    print("8. Buscar libro por autor")
    print("9. Buscar libro por categoría")
    print("10. Listar libros de un usuario")
    print("0. Salir")


def main():

    biblioteca = BibliotecaServicio()

    while True:

        mostrar_menu()

        opcion = input("Seleccione una opción: ")

        if opcion == "1":

            titulo = input("Título: ")
            autor = input("Autor: ")
            categoria = input("Categoría: ")
            isbn = input("ISBN: ")

            biblioteca.agregar_libro(titulo, autor, categoria, isbn)

        elif opcion == "2":

            isbn = input("ISBN del libro: ")
            biblioteca.quitar_libro(isbn)

        elif opcion == "3":

            nombre = input("Nombre del usuario: ")
            id_usuario = input("ID del usuario: ")

            biblioteca.registrar_usuario(nombre, id_usuario)

        elif opcion == "4":

            id_usuario = input("ID del usuario: ")
            biblioteca.eliminar_usuario(id_usuario)

        elif opcion == "5":

            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.prestar_libro(id_usuario, isbn)

        elif opcion == "6":

            id_usuario = input("ID del usuario: ")
            isbn = input("ISBN del libro: ")

            biblioteca.devolver_libro(id_usuario, isbn)

        elif opcion == "7":

            titulo = input("Título del libro: ")
            biblioteca.buscar_por_titulo(titulo)

        elif opcion == "8":

            autor = input("Autor: ")
            biblioteca.buscar_por_autor(autor)

        elif opcion == "9":

            categoria = input("Categoría: ")
            biblioteca.buscar_por_categoria(categoria)

        elif opcion == "10":

            id_usuario = input("ID del usuario: ")
            biblioteca.listar_libros_usuario(id_usuario)

        elif opcion == "0":

            print("Saliendo del sistema...")
            break

        else:

            print("Opción inválida.")


if __name__ == "__main__":
    main()