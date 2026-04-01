from domain.Rocket import Rocket
class RepositoryRocketException(Exception):
    def __init__(self, message):
        self.message = message

class RepositoryInMemoryRocket:
    def __init__(self):
        self.__rocket = None

    def add_rocket(self, rocket):
        """
        Adds a rocket to the repository
        :param rocket: the rocket to be added
        :exception RepositoryRocketException if a rocket has already been added in the repository
        """
        if self.__rocket is not None:
            raise RepositoryRocketException("Rocket already added")
        self.__rocket = rocket

    def get_rocket(self):
        """
        Returns the rocket
        :return: The rocket
        :exception: RepositoryRocketException if rocket is not added
        """
        if self.__rocket is None:
            raise RepositoryRocketException("Rocket not added to memory")
        return self.__rocket

    def delete_rocket(self):
        if self.__rocket is None:
            raise RepositoryRocketException("There is no rocket in the repository")
        self.__rocket = None

class RepositoryFileRocket(RepositoryInMemoryRocket):
    def __init__(self, filename):
        super().__init__()
        self.filename = filename
        self.__load_rocket_from_file()

    def __load_rocket_from_file(self):
        """
        Loads the rocket from the file into memory
        :exception RepositoryRocketException if file is not found
        """
        try:
            with open(self.filename, "r", encoding="utf-8") as file:
                lines = file.readlines()
                lines[0] = lines[0].split(":")
                number_of_engines = lines[0][1].strip()
                number_of_engines = int(number_of_engines)
                lines[1] = lines[1].split(":")
                acceleration_per_engine = lines[1][1].split(" ")[1].strip()
                acceleration_per_engine = float(acceleration_per_engine)
                rocket = Rocket(number_of_engines, acceleration_per_engine)
                super().add_rocket(rocket)

        except IOError:
            raise RepositoryRocketException("File not found")

    def __save_rocket_to_file(self):
        """
        Saves the rocket to the file into memory
        """
        with (open(self.filename, mode="w", encoding="utf-8") as file):
            try:
                rocket = super().get_rocket()
                text = "Number of rocket engines: " + str(rocket.number_of_engines) + "\n" +\
                "Acceleration per engine: " + str(rocket.acceleration_per_engine) + "m/s^2"
            except RepositoryRocketException:
                text = ""
            file.write(text)

    def add_rocket(self, rocket:Rocket):
        super().add_rocket(rocket)
        self.__save_rocket_to_file()

    def get_rocket(self):
        return super().get_rocket()

    def delete_rocket(self):
        super().delete_rocket()
        self.__save_rocket_to_file()