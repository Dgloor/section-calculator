from dataclasses import dataclass
from math import pow, sqrt
from matplotlib import pyplot as plt
import numpy as np


@dataclass
class SeccionT:
    b_alma: float
    h_alma: float
    b_ala: float
    h_ala: float
    espesor: float
    densidad: float

    @staticmethod
    def get_nombre():
        return "Sección T"

    def get_area_alma(self):
        return self.b_alma * self.h_alma

    def get_masa_alma(self):
        volumen_alma = self.get_area_alma() * self.espesor
        return self.densidad * volumen_alma

    def get_area_ala(self):
        return self.b_ala * self.h_ala

    def get_masa_ala(self):
        volumen_ala = self.get_area_ala() * self.espesor
        return self.densidad * volumen_ala

    def get_area_total(self):
        return self.get_area_alma() + self.get_area_ala()

    def get_yi_alma(self):
        return self.h_alma / 2

    def get_yi_ala(self):
        return self.h_alma + (self.h_ala / 2)

    def get_centroide_x(self):
        return self.b_ala / 2

    def get_centroide_y(self):
        a = self.get_area_alma() * self.get_yi_alma()
        b = self.get_area_ala() * self.get_yi_ala()
        return sum([a, b]) / self.get_area_total()

    def get_momento_inercia_x(self):
        a = (1 / 12) * self.b_ala * pow(self.h_ala, 3)
        b = (1 / 12) * self.b_alma * pow(self.h_alma, 3)
        c = pow(self.get_centroide_y() - self.get_yi_ala(), 2) * self.get_area_ala()
        d = pow(self.get_centroide_y() - self.get_yi_alma(), 2) * self.get_area_alma()
        return sum([a, b, c, d])

    def get_momento_inercia_y(self):
        a = (1 / 12) * self.h_ala * pow(self.b_ala, 3)
        b = (1 / 12) * self.h_alma * pow(self.b_alma, 3)
        return sum([a, b])

    def get_radio_giro_x(self):
        return sqrt(self.get_momento_inercia_x() / self.get_area_total())

    def get_radio_giro_y(self):
        return sqrt(self.get_momento_inercia_y() / self.get_area_total())

    def get_peso(self):
        masa = self.get_masa_alma() + self.get_masa_ala()
        peso = masa * 9.8
        return peso

    def get_modulo_seccion(self):
        maxy = max(
            self.h_alma - self.get_centroide_y(), sqrt(pow(self.get_centroide_y(), 2))
        )
        return self.get_momento_inercia_x() / maxy

    def graficar(self):
        plt.title(self.get_nombre())
        color = "blue"

        x_0, y_0 = 0 - (self.b_alma / 2), 0
        x_1, y_1 = x_0 + self.b_alma, 0
        x_2, y_2 = x_0, y_0 + self.h_alma
        x_3, y_3 = x_1, y_1 + self.h_alma
        x_4, y_4 = x_2 - ((self.b_ala - self.b_alma) / 2), y_2
        x_5, y_5 = x_3 + ((self.b_ala - self.b_alma) / 2), y_3
        x_6, y_6 = x_4, y_4 + self.h_ala
        x_7, y_7 = x_5, y_5 + self.h_ala

        plt.plot(np.linspace(x_0, x_1), np.linspace(y_0, y_1), color=color)
        plt.plot(np.linspace(x_0, x_2), np.linspace(y_0, y_2), color=color)
        plt.plot(np.linspace(x_1, x_3), np.linspace(y_1, y_3), color=color)
        plt.plot(np.linspace(x_2, x_4), np.linspace(y_2, y_4), color=color)
        plt.plot(np.linspace(x_3, x_5), np.linspace(y_3, y_5), color=color)
        plt.plot(np.linspace(x_4, x_6), np.linspace(y_4, y_6), color=color)
        plt.plot(np.linspace(x_5, x_7), np.linspace(y_5, y_7), color=color)
        plt.plot(np.linspace(x_6, x_7), np.linspace(y_6, y_7), color=color)

        plt.show()
