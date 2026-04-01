import re
from domain.Planet import Planet

class RepositoryException(Exception):
     def __init__(self, message):
         self.message = message

class PlanetaAlreadyExistsException(RepositoryException):
     def __init__(self):
         self.message = "Planet already stored"

class PlanetaDoesNotExistException(RepositoryException):
    def __init__(self):
        self.message = "Planet is not yet stored"

class RepositoryInMemory:
    def __init__(self):
        self.__planets = {}

    def add_planet(self, planet: Planet):
        """
        Adds a planet to the repository
        :param planet: planet that needs to be added
        :exception: PlanetAlreadyExistsException
        """
        if planet.name in self.__planets:
            raise PlanetaAlreadyExistsException
        self.__planets[planet.name] = planet

    def find_planet(self, name: str) -> Planet:
        """
        Finds a planet by name
        :param name: name of the planet to find
        :exception: PlanetDoesNotExistException
        """
        if name not in self.__planets:
            raise PlanetaDoesNotExistException
        return self.__planets[name]

    def get_all_planets(self) -> list:
        return list(self.__planets.values())

class RepositoryFile(RepositoryInMemory):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.__load_from_file()

    def __load_from_file(self):
        """
        Loads data from file into memory
        :exception: RepositoryException if file is not found
        """
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    if line:
                        parts = re.split(r"[,:=\s]+", line)
                        parts = [p for p in parts if p not in ("diameter", "km", "mass", "Earths")]
                        if parts[0] == "Earth":
                            name = parts[0]
                            diameter = float("12800")
                            mass = float("1")
                        else:
                            name = parts[0]
                            diameter = float(parts[1].strip())
                            mass = float(parts[2].strip())

                        planet = Planet(name, diameter, mass)
                        super().add_planet(planet)

        except IOError:
            raise RepositoryException("File not found")

    def __save_to_file(self):
        """
        Saves data from memory into file
        """
        with open(self.filename, mode="w", encoding="utf-8") as file:
            for planet in super().get_all_planets():
                if planet.name == "Earth":
                    planet_str = "Earth: diameter = 12800 km, mass = 6 * 10^24 kg\n"
                else:
                    planet_str = planet.name + ": diameter = " + str(planet.diameter) + " km, mass = " + str(planet.mass) + " Earths\n"
                file.write(planet_str)

    def add_planet(self, planet: Planet):
        super().add_planet(planet)
        self.__save_to_file()

    def find_planet(self, name: str) -> Planet:
        return super().find_planet(name)

    def get_all_planets(self) -> list:
        return super().get_all_planets()