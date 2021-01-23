from secciones.seccion_t import SeccionT
from secciones.seccion_doble_t import SeccionDobleT
from secciones.seccion_c import SeccionC
from secciones.seccion_g import SeccionG

menuA = """
== Calculadora de Secciones ==
  1. Seccion T
  2. Seccion C
  3. Seccion G
  4. Seccion Doble T
  5. Salir 
"""


def menu_principal():
    op_validas = ["1", "2", "3", "4", "5"]
    op = 0
    while op not in op_validas:
        print(menuA)
        op = input("Ingrese una opción: ")
        if op not in op_validas:
            print("<x> Opción inválida, intente de nuevo <x>")
        return op


def ingreso_seccion(nombre_seccion):
    builders = {
        "seccionT": build_seccion_T,
        "seccionDobleT": build_seccion_doble_T,
        "seccionC": build_seccion_C,
        "seccionG": build_seccion_G,
    }

    return builders[nombre_seccion]()


def ingreso(msj):
    valor = -1

    while valor == -1:
        v = input(msj)
        try:
            n = float(v)
        except ValueError:
            print("Entrada inválida, intente de nuevo <x> ")
        else:
            valor = n

    return valor


def build_seccion_T():
    b_alma = ingreso("Ingrese la base del alma: ")
    h_alma = ingreso("Ingrese la altura del alma: ")
    b_ala = ingreso("Ingrese la base del ala: ")
    h_ala = ingreso("Ingrese la altura del ala: ")
    espesor = ingreso("Ingrese el espesor de la viga: ")
    densidad = ingreso("Ingrese la densidad del material: ")

    return SeccionT(b_alma, h_alma, b_ala, h_ala, espesor, densidad)


def build_seccion_doble_T():
    b_patin_inf = ingreso("Ingrese la base del patín inferior: ")
    h_patin_inf = ingreso("Ingrese la altura del patín inferior: ")
    b_patin_sup = ingreso("Ingrese la base del patín superior: ")
    h_patin_sup = ingreso("Ingrese la altura del patín superior: ")
    b_alma = ingreso("Ingrese la base del alma: ")
    penalte = ingreso("Ingrese penalte: ")
    espesor = ingreso("Ingrese el espesor de la viga: ")
    densidad = ingreso("Ingrese la densidad del material: ")

    return SeccionDobleT(
        b_patin_inf,
        h_patin_inf,
        b_patin_sup,
        h_patin_sup,
        b_alma,
        penalte,
        espesor,
        densidad,
    )


def build_seccion_C():
    b_alma = ingreso("Ingrese la base del alma: ")
    h_alma = ingreso("Ingrese la altura del alma: ")
    b_patin_inf = ingreso("Ingrese la base del patín inferior: ")
    h_patin_inf = ingreso("Ingrese la altura del patín inferior: ")
    b_patin_sup = ingreso("Ingrese la base del patín superior: ")
    h_patin_sup = ingreso("Ingrese la altura del patín superior: ")
    espesor = ingreso("Ingrese el espesor de la viga: ")
    densidad = ingreso("Ingrese la densidad del material: ")

    return SeccionC(
        b_alma,
        h_alma,
        b_patin_inf,
        h_patin_inf,
        b_patin_sup,
        h_patin_sup,
        espesor,
        densidad,
    )


def build_seccion_G():
    h_alma = ingreso("Ingrese la altura del alma: ")
    b_patin_inf = ingreso("Ingrese la base del patín inferior: ")
    b_patin_sup = ingreso("Ingrese la base del patín superior: ")
    h_gancho_inf = ingreso("Ingrese la altura del gancho inferior: ")
    h_gancho_sup = ingreso("Ingrese la altura del gancho superior: ")
    espesor = ingreso("Ingrese el espesor de los patines y ganchos: ")
    espesor_viga = ingreso("Ingrese la espesor de la viga: ")
    densidad = ingreso("Ingrese la densidad del material: ")

    return SeccionG(
        h_alma,
        b_patin_inf,
        b_patin_sup,
        h_gancho_inf,
        h_gancho_sup,
        espesor,
        espesor_viga,
        densidad,
    )


def mostrar_info(seccion):
    print(f"== Datos {seccion.get_nombre()} ==")
    print("{:<20}{:>20.2f}".format("Área: ", seccion.get_area_total()))
    print("{:<20}{:>20.2f}".format("Centroide X: ", seccion.get_centroide_x()))
    print("{:<20}{:>20.2f}".format("Centroide Y: ", seccion.get_centroide_y()))
    print("{:<20}{:>20.2f}".format("Inercia X: ", seccion.get_momento_inercia_x()))
    print("{:<20}{:>20.2f}".format("Inercia Y: ", seccion.get_momento_inercia_y()))
    print("{:<20}{:>20.2f}".format("Radio Giro X: ", seccion.get_radio_giro_x()))
    print("{:<20}{:>20.2f}".format("Radio Giro Y: ", seccion.get_radio_giro_y()))
    print("{:<20}{:>20.2f}".format("Módulo sección: ", seccion.get_modulo_seccion()))
    print("{:<20}{:>20.2f}".format("Peso: ", seccion.get_peso()))
    print()


def mostrar_grafica(seccion):
    mostrar = ""
    while mostrar != "s" and mostrar != "n":
        mostrar = input("Mostrar gráfica (s/n): ")
        if mostrar == "s":
            print(f"\nGráfica de la {seccion.get_nombre()}")
            seccion.graficar()
        elif mostrar != "s" and mostrar != "n":
            print("Opción invalida, intente de nuevo.")
