class Planet:
    def __init__(self, name, diameter, mass, period=None, orbital_radius=None):
        self.__name = name
        self.__diameter = diameter
        self.__mass = mass
        self.__period = period
        self.__orbital_radius = orbital_radius

    @property
    def name(self):
        return self.__name

    @property
    def mass(self):
        return self.__mass

    @property
    def diameter(self):
        return self.__diameter

    @property
    def period(self):
        return self.__period

    @property
    def orbital_radius(self):
        return self.__orbital_radius

    @mass.setter
    def mass(self, mass):
        self.__mass = mass

    @diameter.setter
    def diameter(self, diameter):
        self.__diameter = diameter

    @period.setter
    def period(self, period):
        self.__period = period

    @orbital_radius.setter
    def orbital_radius(self, orbital_radius):
        self.__orbital_radius = orbital_radius

    def __eq__(self, other):
        return self.name == other.name and self.diameter == other.diameter and self.mass == other.mass

    def __str__(self, lang = "en"):
        if lang == "1":
            return f"Name: {self.__name:<10} | Diameter: {self.__diameter:<10} | Mass: {self.__mass:<10}"
        else:
            return f"Nume: {self.__name:<10} | Diametru: {self.__diameter:<10}| Masă: {self.__mass:<10}"