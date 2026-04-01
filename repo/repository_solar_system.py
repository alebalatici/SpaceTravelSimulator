from repo.repository_planetary_data import *
class RepositorySolarSystemException(Exception):
    def __init__(self, message):
        self.message = message

class RepositoryFileSolarSystem:
    def __init__(self, filename, planet_filename):
        self.__repo_planet = RepositoryFile(planet_filename)
        self.filename = filename
        self.load_planets_from_file()

    def load_planets_from_file(self):
        """
        Loads the periods and the orbital radius from the file
        :return: IO Error if file is not found
        """
        try:
            with open(self.filename, mode="r", encoding="utf-8") as file:
                lines = file.readlines()
                for line in lines:
                    if line:
                        parts = re.split(r"[:=]", line)
                        name = parts[0].strip()
                        parts[2] = parts[2].strip()
                        period = int(parts[2].split(" ")[0])
                        parts[3] = parts[3].strip()
                        orbital_radius = float(parts[3].split(" ")[0])

                        planet = self.__repo_planet.find_planet(name)
                        planet.period = period
                        planet.orbital_radius = orbital_radius

        except IOError:
            raise RepositoryException("File not found")

    def get_all_planets_extended(self):
        """
        Returns the list of all planets extended in the repository, with the period and the orbital radius
        :return: the list of all planets extended in the repository, with the period and the orbital radius
        """
        return self.__repo_planet.get_all_planets()

    def find_planet_extended(self, name):
        """
        Returns the planet with the name name from the repository, with the period and the orbital radius
        :param name: The name of the planet
        :return: The planet with the name name from the repository, with the period and the orbital radius
        """
        return self.__repo_planet.find_planet(name)

    def __save_to_file(self):
        """
        Saves the planets to the file
        """
        with open(self.filename, mode="w", encoding="utf-8") as file:
            for planet in self.__repo_planet.get_all_planets():
                planet_str = str(planet.name) + ": period = " + str(planet.period) + " days, orbital radius = " + str(planet.orbital_radius) + " AU\n"
                file.write(planet_str)