class Rocket:
    def __init__(self, number_of_engines, acceleration_per_engine):
        self.__number_of_engines = number_of_engines
        self.__acceleration_per_engine = acceleration_per_engine

    @property
    def number_of_engines(self):
        return self.__number_of_engines

    @property
    def acceleration_per_engine(self):
        return self.__acceleration_per_engine

    def __eq__(self, other):
        return self.__number_of_engines == other.number_of_engines and self.__acceleration_per_engine == other.acceleration_per_engine

    def __str__(self, lang = "en"):
        if lang == "1":
            return f"Number of engines: {self.__number_of_engines} | Acceleration per engine: {self.__acceleration_per_engine}"
        else:
            return f"Numarul de motoare: {self.__number_of_engines} | Acceleratia unui motor: {self.__acceleration_per_engine}"
