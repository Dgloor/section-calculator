from dataclasses import dataclass
from math import pow, sqrt
from matplotlib import pyplot as plt
import numpy as np


@dataclass
class SeccionG:
    h_alma: float
    b_patin_inf: float
    b_patin_sup: float
    h_gancho_inf: float
    h_gancho_sup: float
    espesor: float
    espesor_viga: float
    densidad: float

    @staticmethod
    def get_nombre():
        return "Sección G"

    def get_area_alma(self):
        return self.h_alma * self.espesor

    def get_masa_alma(self):
        volumen = self.get_area_alma() * self.espesor_viga
        return volumen * self.densidad

    def get_area_patin_inf(self):
        return self.b_patin_inf * self.espesor

    def get_masa_patin_inf(self):
        volumen = self.get_area_patin_inf() * self.espesor_viga
        return volumen * self.densidad

    def get_area_patin_sup(self):
        return self.b_patin_sup * self.espesor

    def get_masa_patin_sup(self):
        volumen = self.get_area_patin_sup() * self.espesor_viga
        return volumen * self.densidad

    def get_area_gancho_inf(self):
        return self.h_gancho_inf * self.espesor

    def get_masa_gancho_inf(self):
        volumen = self.get_area_gancho_inf() * self.espesor_viga
        return volumen * self.densidad

    def get_masa_gancho_sup(self):
        volumen = self.get_area_gancho_sup() * self.espesor_viga
        return volumen * self.densidad

    def get_area_gancho_sup(self):
        return self.h_gancho_sup * self.espesor

    def get_area_total(self):
        return (
            self.get_area_alma()
            + self.get_area_patin_sup()
            + self.get_area_patin_inf()
            + self.get_area_gancho_sup()
            + self.get_area_gancho_inf()
        )

    def get_yi_alma(self):
        return self.h_alma / 2

    def get_yi_patin_inf(self):
        return self.espesor / 2

    def get_yi_patin_sup(self):
        return self.h_alma - (self.espesor / 2)

    def get_yi_gancho_inf(self):
        return self.h_gancho_inf / 2

    def get_yi_gancho_sup(self):
        return self.h_alma - (self.h_gancho_sup / 2)

    def get_xi_alma(self):
        return self.espesor / 2

    def get_xi_patin_inf(self):
        return self.espesor + (self.b_patin_inf / 2)

    def get_xi_patin_sup(self):
        return self.espesor + (self.b_patin_sup / 2)

    def get_xi_gancho_inf(self):
        return self.espesor + self.b_patin_inf + (self.espesor / 2)

    def get_xi_gancho_sup(self):
        return self.espesor + self.b_patin_sup + (self.espesor / 2)

    def get_centroide_x(self):
        a = self.get_area_alma() * self.get_xi_alma()
        b = self.get_area_patin_inf() * self.get_xi_patin_inf()
        c = self.get_area_patin_sup() * self.get_xi_patin_sup()
        d = self.get_area_gancho_inf() * self.get_xi_gancho_inf()
        e = self.get_area_gancho_sup() * self.get_xi_gancho_sup()
        return sum([a, b, c, d, e]) / self.get_area_total()

    def get_centroide_y(self):
        a = self.get_area_alma() * self.get_yi_alma()
        b = self.get_area_patin_inf() * self.get_yi_patin_inf()
        c = self.get_area_patin_sup() * self.get_yi_patin_sup()
        d = self.get_area_gancho_inf() * self.get_yi_gancho_inf()
        e = self.get_area_gancho_sup() * self.get_yi_gancho_sup()
        return sum([a, b, c, d, e]) / self.get_area_total()

    def get_momento_inercia_x(self):
        a = (1 / 12) * self.espesor * pow(self.h_alma, 3)
        b = (1 / 12) * self.espesor * pow(self.h_gancho_sup, 3)
        c = (1 / 12) * self.espesor * pow(self.h_gancho_inf, 3)
        d = (1 / 12) * self.b_patin_inf * pow(self.espesor, 3)
        e = (1 / 12) * self.b_patin_sup * pow(self.espesor, 3)
        f = (
            pow(self.get_centroide_y() - self.get_yi_gancho_sup(), 2)
            * self.get_area_gancho_sup()
        )
        g = (
            pow(self.get_centroide_y() - self.get_yi_gancho_inf(), 2)
            * self.get_area_gancho_inf()
        )
        h = (
            pow(self.get_centroide_y() - self.get_yi_patin_sup(), 2)
            * self.get_area_patin_sup()
        )
        i = (
            pow(self.get_centroide_y() - self.get_yi_patin_inf(), 2)
            * self.get_area_patin_inf()
        )
        j = pow(self.get_centroide_y() - self.get_yi_alma(), 2) * self.get_area_alma()
        return sum([a, b, c, d, e, f, g, h, i, j])

    def get_momento_inercia_y(self):
        a = (1 / 12) * self.h_alma * pow(self.espesor, 3)
        b = (1 / 12) * self.h_gancho_sup * pow(self.espesor, 3)
        c = (1 / 12) * self.h_gancho_inf * pow(self.espesor, 3)
        d = (1 / 12) * self.espesor * pow(self.b_patin_inf, 3)
        e = (1 / 12) * self.espesor * pow(self.b_patin_sup, 3)
        f = (
            pow(self.get_centroide_x() - self.get_xi_gancho_sup(), 2)
            * self.get_area_gancho_sup()
        )
        g = (
            pow(self.get_centroide_x() - self.get_xi_gancho_inf(), 2)
            * self.get_area_gancho_inf()
        )
        h = (
            pow(self.get_centroide_x() - self.get_xi_patin_sup(), 2)
            * self.get_area_patin_sup()
        )
        i = (
            pow(self.get_centroide_x() - self.get_xi_patin_inf(), 2)
            * self.get_area_patin_inf()
        )
        j = pow(self.get_centroide_x() - self.get_xi_alma(), 2) * self.get_area_alma()
        return sum([a, b, c, d, e, f, g, h, i, j])

    def get_radio_giro_x(self):
        return sqrt(self.get_momento_inercia_x() / self.get_area_total())

    def get_radio_giro_y(self):
        return sqrt(self.get_momento_inercia_y() / self.get_area_total())

    def get_peso(self):
        masa = (
            self.get_masa_alma()
            + self.get_masa_patin_inf()
            + self.get_masa_patin_sup()
            + self.get_masa_gancho_inf()
            + self.get_masa_gancho_sup()
        )
        peso = masa * 9.8
        return peso

    def get_modulo_seccion(self):
        return self.get_momento_inercia_x() / (self.h_alma / 2)

    def graficar(self):
        plt.title(self.get_nombre())
        color = "blue"

        x_0, y_0 = 0, 0
        x_1, y_1 = x_0 + self.b_patin_inf, y_0
        x_2, y_2 = x_1, y_1 + self.h_gancho_inf
        x_3, y_3 = x_2 - self.espesor, y_2
        x_4, y_4 = x_3, y_3 - self.h_gancho_inf + self.espesor
        x_5, y_5 = x_4 - self.b_patin_inf + (self.espesor * 2), y_4
        x_6, y_6 = x_5, y_5 + self.h_alma - (self.espesor * 2)
        x_7, y_7 = x_6 + self.b_patin_sup - (self.espesor * 2), y_6
        x_8, y_8 = x_7, y_7 - self.h_gancho_sup + self.espesor
        x_9, y_9 = x_8 + self.espesor, y_8
        x_10, y_10 = x_9, y_9 + self.h_gancho_sup
        x_11, y_11 = x_10 - self.b_patin_sup, y_10

        plt.plot(np.linspace(x_0, x_1), np.linspace(y_0, y_1), color=color)
        plt.plot(np.linspace(x_1, x_2), np.linspace(y_1, y_2), color=color)
        plt.plot(np.linspace(x_2, x_3), np.linspace(y_2, y_3), color=color)
        plt.plot(np.linspace(x_3, x_4), np.linspace(y_3, y_4), color=color)
        plt.plot(np.linspace(x_4, x_5), np.linspace(y_4, y_5), color=color)
        plt.plot(np.linspace(x_5, x_6), np.linspace(y_5, y_6), color=color)
        plt.plot(np.linspace(x_6, x_7), np.linspace(y_6, y_7), color=color)
        plt.plot(np.linspace(x_7, x_8), np.linspace(y_7, y_8), color=color)
        plt.plot(np.linspace(x_8, x_9), np.linspace(y_8, y_9), color=color)
        plt.plot(np.linspace(x_9, x_10), np.linspace(y_9, y_10), color=color)
        plt.plot(np.linspace(x_10, x_11), np.linspace(y_10, y_11), color=color)
        plt.plot(np.linspace(x_11, x_0), np.linspace(y_11, y_0), color=color)

        plt.show()
