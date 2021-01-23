from dataclasses import dataclass
from math import pow, sqrt
from matplotlib import pyplot as plt
import numpy as np


@dataclass
class SeccionDobleT:
    b_patin_inf: float
    h_patin_inf: float
    b_patin_sup: float
    h_patin_sup: float
    b_alma: float
    peralte: float
    espesor: float
    densidad: float

    @staticmethod
    def get_nombre():
        return "Sección Doble T"

    def get_h_alma(self):
        return self.peralte - self.h_patin_inf - self.h_patin_sup

    def get_area_alma(self):
        return self.b_alma * self.get_h_alma()

    def get_masa_alma(self):
        volumen = self.get_area_alma() * self.espesor
        return self.densidad * volumen

    def get_area_patin_sup(self):
        return self.b_patin_sup * self.h_patin_sup

    def get_masa_patin_sup(self):
        volumen = self.get_area_patin_sup() * self.espesor
        return self.densidad * volumen

    def get_area_patin_inf(self):
        return self.b_patin_inf * self.h_patin_inf

    def get_masa_patin_inf(self):
        volumen = self.get_area_patin_inf() * self.espesor
        return self.densidad * volumen

    def get_area_total(self):
        return (
            self.get_area_alma() + self.get_area_patin_sup() + self.get_area_patin_inf()
        )

    def get_yi_alma(self):
        return (self.get_h_alma() / 2) + self.h_patin_inf

    def get_yi_patin_sup(self):
        return self.peralte - (self.h_patin_sup / 2)

    def get_yi_patin_inf(self):
        return self.h_patin_sup / 2

    def get_centroide_x(self):
        return self.b_patin_sup / 2

    def get_centroide_y(self):
        a = self.get_area_alma() * self.get_yi_alma()
        b = self.get_area_patin_inf() * self.get_yi_patin_inf()
        c = self.get_area_patin_sup() * self.get_yi_patin_sup()
        return sum([a, b, c]) / self.get_area_total()

    def get_momento_inercia_x(self):
        a = (1 / 12) * self.b_patin_inf * pow(self.h_patin_inf, 3)
        b = (1 / 12) * self.b_alma * pow(self.get_h_alma(), 3)
        c = (1 / 12) * self.h_patin_sup * pow(self.b_patin_sup, 3)
        d = (
            pow(self.get_centroide_y() - self.get_yi_patin_inf(), 2)
            * self.get_area_patin_inf()
        )
        e = (
            pow(self.get_centroide_y() - self.get_yi_patin_sup(), 2)
            * self.get_area_patin_sup()
        )
        f = pow(self.get_centroide_y() - self.get_yi_alma(), 2) * self.get_area_alma()
        return sum([a, b, c, d, e, f])

    def get_momento_inercia_y(self):
        a = (1 / 12) * self.h_patin_inf * pow(self.b_patin_inf, 3)
        b = (1 / 12) * self.h_patin_sup * pow(self.b_patin_sup, 3)
        c = (1 / 12) * self.get_h_alma() * pow(self.b_alma, 3)
        return sum([a, b, c])

    def get_radio_giro_x(self):
        return sqrt(self.get_momento_inercia_x() / self.get_area_total())

    def get_radio_giro_y(self):
        return sqrt(self.get_momento_inercia_y() / self.get_area_total())

    def get_peso(self):
        masa = (
            self.get_masa_patin_sup() + self.get_masa_patin_inf() + self.get_masa_alma()
        )
        peso = masa * 9.8
        return peso

    def get_modulo_seccion(self):
        return self.get_momento_inercia_x() / (self.peralte / 2)

    def graficar(self):
        plt.title(self.get_nombre())
        color = "blue"

        x_0, y_0 = 0 - (self.b_patin_inf / 2), 0
        x_1, y_1 = x_0 + self.b_patin_inf, y_0
        x_2, y_2 = x_0, y_0 + self.h_patin_inf
        x_3, y_3 = x_1, y_1 + self.h_patin_inf
        x_4, y_4 = x_2 + (self.b_patin_inf / 2) - (self.b_alma / 2), y_2
        x_5, y_5 = x_3 - (self.b_patin_inf / 2) + (self.b_alma / 2), y_3
        x_6, y_6 = x_4, y_4 + self.get_h_alma()
        x_7, y_7 = x_5, y_5 + self.get_h_alma()
        x_8, y_8 = x_6 - ((self.b_patin_sup - self.b_alma) / 2), y_6
        x_9, y_9 = x_7 + ((self.b_patin_sup - self.b_alma) / 2), y_7
        x_10, y_10 = x_8, y_8 + self.h_patin_sup
        x_11, y_11 = x_9, y_9 + self.h_patin_sup

        plt.plot(np.linspace(x_0, x_1), np.linspace(y_0, y_1), color=color)
        plt.plot(np.linspace(x_0, x_2), np.linspace(y_0, y_2), color=color)
        plt.plot(np.linspace(x_1, x_3), np.linspace(y_1, y_3), color=color)
        plt.plot(np.linspace(x_2, x_4), np.linspace(y_2, y_4), color=color)
        plt.plot(np.linspace(x_3, x_5), np.linspace(y_3, y_5), color=color)
        plt.plot(np.linspace(x_4, x_6), np.linspace(y_4, y_6), color=color)
        plt.plot(np.linspace(x_5, x_7), np.linspace(y_5, y_7), color=color)
        plt.plot(np.linspace(x_6, x_8), np.linspace(y_6, y_8), color=color)
        plt.plot(np.linspace(x_7, x_9), np.linspace(y_7, y_9), color=color)
        plt.plot(np.linspace(x_8, x_10), np.linspace(y_8, y_10), color=color)
        plt.plot(np.linspace(x_9, x_11), np.linspace(y_9, y_11), color=color)
        plt.plot(np.linspace(x_10, x_11), np.linspace(y_10, y_11), color=color)

        plt.show()
