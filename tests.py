from secciones.seccion_t import SeccionT
from secciones.seccion_doble_t import SeccionDobleT
from secciones.seccion_c import SeccionC
from secciones.seccion_g import SeccionG


def probar_seccion(seccion):
    print(seccion)
    area = seccion.get_area_total()
    print(f"area: {area}")
    centroide = seccion.get_centroide_x(), seccion.get_centroide_y()
    print(f"centroide (x,y): {centroide}")
    m_inercia = seccion.get_momento_inercia_x(), seccion.get_momento_inercia_y()
    print(f"momento de inercia (x,y): {m_inercia}")
    radio_giro = seccion.get_radio_giro_x(), seccion.get_radio_giro_y()
    print(f"radio de giro (x,y): {radio_giro}")
    peso = seccion.get_peso()
    print(f"peso: {peso}")
    modulo_seccion = seccion.get_modulo_seccion()
    print(f"modulo sección: {modulo_seccion}")
    print()
    seccion.graficar()


if __name__ == "__main__":
    st = SeccionT(3, 17, 20, 3, 0.1, 7.85)
    sdt = SeccionDobleT(46, 5.20, 46, 5.20, 3.8, 80, 5, 7.85)
    sc = SeccionC(1.8, 25.50 - (2 * 1.8), 48.5, 1.8, 48.8, 1.8, 1.5, 7.85)
    cg = SeccionG(25, 10, 10, 6, 6, 2, 0.1, 7.85)

    probar_seccion(st)
    probar_seccion(sdt)
    probar_seccion(sc)
    probar_seccion(cg)
