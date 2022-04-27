
class Entregable():
    __entregado = False

    def entregar(self):
        self.__entregado = True

    def devolver(self):
        self.__entregado = False

    def isEntregado(self):
        return self.__entregado

    def numMax(self, lista):
        return max(lista, key=lambda item: item[1])

class Serie(Entregable):
    __titulo = ""
    __numero_temporadas = 0
    __genero = ""
    __creador = ""

    @property
    def titulo(self):
        return self.__titulo

    @property
    def numero_temporadas(self):
        return self.__numero_temporadas

    @property
    def genero(self):
        return self.__genero

    @property
    def creador(self):
        return self.__creador

    @titulo.setter
    def set_titulo(self, titulo):
        self.__titulo = titulo

    @numero_temporadas.setter
    def set_numero_temporadas(self, numero_temporadas):
        self.__numero_temporadas = numero_temporadas

    @genero.setter
    def set_genero(self, genero):
        self.__genero = genero

    @creador.setter
    def set_creador(self, creador):
        self.__creador = creador

    def __init__(self, titulo, genero, creador, num_temp = 3):
        self.__titulo = titulo
        self.__numero_temporadas = num_temp
        self.__genero = genero
        self.__creador = creador

    def __str__(self):
        return f"Título: {self.__titulo}, Número de temporadas: {self.__numero_temporadas}, Género: {self.__genero}, Creador: {self.__creador}"


class Videojuego(Entregable):
    __titulo = ""
    __horas_estimadas = 0
    __genero = ""
    __compania = ""

    @property
    def titulo(self):
        return self.__titulo

    @property
    def horas_estimadas(self):
        return self.__horas_estimadas

    @property
    def genero(self):
        return self.__genero

    @property
    def compania(self):
        return self.__compania

    @titulo.setter
    def set_titulo(self, titulo):
        self.__titulo = titulo

    @horas_estimadas.setter
    def set_horas_estimadas(self, horas_estimadas):
        self.__horas_estimadas = horas_estimadas

    @genero.setter
    def set_genero(self, genero):
        self.__genero = genero

    @compania.setter
    def set_compañia(self, compania):
        self.__compania = compania


    def __init__(self, titulo, genero, compania, horas = 10):
        self.__titulo = titulo
        self.__horas_estimadas = horas
        self.__genero = genero
        self.__compania = compania

    def __str__(self):
        return f"Título: {self.__titulo}, Horas estimadas: {self.__horas_estimadas}, Género: {self.__genero}, Compañía: {self.__compania}"


if __name__ == '__main__':
    series = [Serie("Serie 1", "Acción", "Netflix"), Serie("Serie 2", "Drama", "Amazon"), Serie("Serie 3", "Comedia", "HBO", 8),
              Serie("Serie 4", "Policíaca", "Netflix", 6), Serie("Serie 5", "Bélico", "HBO")]
    videojuegos = [Videojuego("Juego 1", "RPG", "Bethesda"), Videojuego("Juego 2", "Estrategia", "Compañia 2", 18),
                   Videojuego("Juego 3", "Acción", "Compàñia 2", 16), Videojuego("Juego 4", "MMORPG", "Compañia 3"),
                   Videojuego("Juego 5", "Aventura gráfica", "Compañia 1")]

    series[0].entregar()
    series[2].entregar()
    videojuegos[1].entregar()
    videojuegos[3].entregar()

    contSeries = 0
    contJuegos = 0
    serieMaxHoras = 0
    juegoMaxHoras = 0

    for serie in series:
        if serie.isEntregado():
            contSeries += 1
            serie.devolver()
        if serie.numero_temporadas > serieMaxHoras:
            serieMaxHoras = serie.numero_temporadas

    for juego in videojuegos:
        if juego.isEntregado():
            contJuegos += 1
            juego.devolver()
        if juego.horas_estimadas > juegoMaxHoras:
            juegoMaxHoras = juego.horas_estimadas

    print(f"Series entregadas: {contSeries} -- Juegos entregados: {contJuegos}")

    for s in series:
        if s.numero_temporadas == serieMaxHoras:
            print(s)
    for j in videojuegos:
        if j.horas_estimadas == juegoMaxHoras:
            print(j)