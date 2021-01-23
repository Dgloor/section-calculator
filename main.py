from inputs import menu_principal, ingreso_seccion, mostrar_info, mostrar_grafica

if __name__ == "__main__":
    op = ""
    seccion = None
    while op != "5":
        op = menu_principal()
        print()

        if op == "1":
            seccion = ingreso_seccion("seccionT")
        elif op == "2":
            seccion = ingreso_seccion("seccionC")
        elif op == "3":
            seccion = ingreso_seccion("seccionG")
        elif op == "4":
            seccion = ingreso_seccion("seccionDobleT")
        elif op == "5":
            print("</> Programa finalizado </>")
            exit()

        print()
        if seccion != None:
            mostrar_info(seccion)
            mostrar_grafica(seccion)
