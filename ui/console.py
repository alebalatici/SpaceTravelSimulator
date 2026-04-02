from repo.repository_planetary_data import RepositoryFile, RepositoryException
from repo.repository_rocket_data import RepositoryFileRocket
from repo.repository_solar_system import RepositoryFileSolarSystem
from source.services import *
from ui.printer import Printer, Printer_Ui_Exception

class ui_exception(Exception):
    def __init__(self, message):
        self.message = message

class Console:
    def __init__(self, lang=""):
        self.__repo_planets = None
        self.__repo_rocket = None
        self.__repo_solar_system = None
        self.__lang = lang
        self.__filename_planets = None
        self.__filename_rocket = None
        self.__filename_solar_system = None
        self.__srv = ServicesCalculations()
        self.__printer = Printer(lang)

    def print_all_planets(self):
        try:
            if self.__repo_planets is None: #
                self.__printer.print_select_planet_file_text()
                filename = self.__printer.print_file_menu()
                self.__filename_planets = filename
                self.__repo_planets = RepositoryFile(filename)

            planets = self.__repo_planets.get_all_planets()
            for planet in planets:
                print(planet.__str__(lang=self.__lang))
        except ui_exception as e:
            print(e)

        except Printer_Ui_Exception as e:
            print(e)

    def calculate_escape_velocity_ui(self):
        try:

            if self.__repo_planets is None:
                self.__printer.print_select_planet_file_text()
                filename = self.__printer.print_file_menu()
                self.__filename_planets = filename
                self.__repo_planets = RepositoryFile(filename)

            if self.__lang == "1":
                print(f"{'Planet Name':<12} | {'Escape Velocity':<12}")
            else:
                print(f"{'Nume planetă':<10} | {'Viteză de evadare':<10}")
            print("_" * 35)
            planets = self.__repo_planets.get_all_planets()
            for planet in planets:
                escape_velocity = self.__srv.escape_velocity_planet(planet)
                print(f"{planet.name:<12} | {math.ceil(escape_velocity)} m/s")
            print("_" * 35)
        except ui_exception as e:
            print(e)
        except Printer_Ui_Exception as e:
            print(e)

    def calculate_time_distance_escape_velocity_ui(self):
        try:
            if self.__repo_planets is None:
                self.set_planet_repo_file()
            if self.__repo_rocket is None:
                self.set_rocket_repo_file()
            rocket = self.__repo_rocket.get_rocket()
            planets = self.__repo_planets.get_all_planets()

            print("_" * 130)
            if self.__lang == "1":
                print(f"{'Planet Name':<20} | {'Time to reach escape velocity':>32} | {'Distance to reach escape velocity':>30} | {'The distance from center':>35}")
            else:
                print(
                    f"{'Numele Planetei':<20} | {'Timpul pentru viteza de evadare':>32} | {'Distanta pentru viteza de evadare':>30} | {'Distanta de la centru':>35}")
            print("_" * 130)
            for planet in planets:
                time = self.__srv.time_escape_velocity(planet, rocket)
                distance = self.__srv.distance_escape_velocity(0, planet, rocket)
                distance_from_centre = self.__srv.distance_centre_escape_velocity(0, planet, rocket)
                print(f"{planet.name:<20} | {math.floor(time):>30} s | {math.floor(distance):>31} m | {math.floor(distance_from_centre):>34} m")
            print("_" * 130)

        except ui_exception as e:
            print(e)

        except Printer_Ui_Exception as e:
            print(e)

    def change_language(self):
        if self.__lang == "1":
            self.__lang = "2"
            self.__printer = Printer(self.__lang)
            print("Limba noua: Romana")
        else:
            self.__lang = "1"
            self.__printer = Printer(self.__lang)
            print("New Language: English")

    def select_a_planet_menu(self):
        planet = None
        while True:
            planet_name = input(">>>").lower().strip().capitalize()
            try:
                planet = self.__repo_solar_system.find_planet_extended(planet_name)
                break

            except RepositoryException:
                if self.__lang == "1":
                    print(f"There hasn't been found any planet with the name {planet_name}.")
                else:
                    print(f"Nu a fost gasita nicio planeta cu numele {planet_name}.")
                self.__printer.print_loop_menu()
                option = input()
                match option:
                    case "1":
                        continue
                    case "2":
                        return None
                    case _:
                        if self.__lang == "1":
                            print("Invalid input.")
                        else:
                            print("Optiune invalida.")
        return planet

    def stage_3_5_6_select_planets(self):
        if self.__lang == "1":
            print("Let the journey begin! Please enter the name of the starting planet: ")
        else:
            print("Sa inceapa calatoria! Va rugam introduceti numele planetei de unde incepe calatoria: ")

        starting_planet = self.select_a_planet_menu()
        if starting_planet is None:
            return
        if self.__lang == "1":
            print(
                f"Selected planet: {starting_planet.name} | Period: {starting_planet.period} Days | Orbital Radius: {starting_planet.orbital_radius} AU")
        else:
            print(
                f"Planeta selectata: {starting_planet.name} | Perioada: {starting_planet.period} Zile| Raza Orbitală: {starting_planet.orbital_radius} AU")

        if self.__lang == "1":
            print(f"Please enter the name of the destination planet: ")
        else:
            print(f"Va rugam introduceti numele planetei destinatie: ")

        destination_planet = self.select_a_planet_menu()
        if destination_planet is None:
            return
        if self.__lang == "1":
            print(
                f"Selected planet: {destination_planet.name} | Period: {destination_planet.period} Days | Orbital Radius: {destination_planet.orbital_radius} AU")
        else:
            print(
                f"Planeta selectata: {destination_planet.name} | Perioada: {destination_planet.period} Zile| Raza Orbitală: {destination_planet.orbital_radius} AU")
        return starting_planet, destination_planet

    def stage_3_ui(self):
        try:
            if self.__repo_planets is None:
                self.set_planet_repo_file()
            if self.__repo_rocket is None:
                self.set_rocket_repo_file()
            if self.__repo_solar_system is None:
                self.set_solar_system_repo_file()

            starting_planet, destination_planet = self.stage_3_5_6_select_planets()

            rocket = self.__repo_rocket.get_rocket()
            self.stage_3_ui_printing_data(starting_planet, destination_planet, rocket)

        except ui_exception as e:
            print(e)

        except Printer_Ui_Exception as e:
            print(e)

        except ValueError as e:
            print(e)

        except TypeError as e:
            if self.__lang == "1":
                print("Exiting...")
            else:
                print("Iesire...")

    def stage_3_ui_printing_data(self, starting_planet, destination_planet, rocket):
        print("_" * 150)
        if self.__lang == "1":
            print(f"Note: We assume that our rocket stops by doing what they did to get going, but in reverse")
        else:
            print(f"Notă: Presupunem că racheta noastră se oprește făcând ceea ce a făcut pentru a porni, dar în sens invers")

        print(f"{starting_planet.name} ---> {destination_planet.name}")
        planet =  self.__srv.maximum_escape_velocity(starting_planet, destination_planet)
        time = self.__srv.time_escape_velocity(planet, rocket)
        distance = self.__srv.distance_escape_velocity(0, planet, rocket)
        cruising_distance = self.__srv.cruising_distance(starting_planet, destination_planet, rocket)
        cruising_time = self.__srv.cruising_time(starting_planet, destination_planet, rocket)
        total_cruising_time = self.__srv.total_cruising_time(starting_planet, destination_planet, rocket)

        self.__printer.stage_3_5_6_ui_printing_data(time, distance, cruising_distance, cruising_time, total_cruising_time)
        print("_" * 150)

    def set_planet_repo_file(self):
        self.__printer.print_select_planet_file_text()
        filename_planet = self.__printer.print_file_menu()
        self.__filename_planets = filename_planet
        self.__repo_planets = RepositoryFile(filename_planet)

    def set_rocket_repo_file(self):
        self.__printer.print_select_rocket_file_text()
        filename_rocket = self.__printer.print_file_menu_rocket()
        self.__filename_rocket = filename_rocket
        self.__repo_rocket = RepositoryFileRocket(filename_rocket)

    def set_solar_system_repo_file(self):
        self.__printer.print_select_solar_system_file_text()
        filename_solar_system = self.__printer.print_file_menu_solar_system()
        self.__filename_solar_system = filename_solar_system
        self.__repo_solar_system = RepositoryFileSolarSystem(filename_solar_system, self.__filename_planets)

    def display_the_angular_position_of_each_planet(self):
        try:
            if self.__repo_planets is None:
                self.set_planet_repo_file()

            if self.__repo_solar_system is None:
                self.set_solar_system_repo_file()

            if self.__lang == "1":
                text = "Enter the number of days: "
            else:
                text = "Introduceti numarul de zile: "

            number_of_days = int(input(text))

            self.print_planets_with_angular_position(number_of_days)

        except ui_exception as e:
            print(e)

        except ValueError as e:
            if self.__lang == "1":
                print("Error: The number of days has to be an integer")
            else:
                print("Eroare: Numarul de zile trebuie sa fie un intreg")

        except Printer_Ui_Exception as e:
            print(e)

    def print_planets_with_angular_position(self, number_of_days):
        print("_" * 45)
        if self.__lang == "1":
            print(f"{'Planet Name':<20} | {'Angular Position':>22}")
        else:
            print(f"{'Nume planetă':<20} | {'Poziția Unghiulară':>22}")
        print("_" * 45)
        planets = self.__repo_solar_system.get_all_planets_extended()
        for planet in planets:
            angular_position = self.__srv.angular_position(planet, number_of_days)
            if self.__lang == "1":
                print(f"{planet.name:<20} | {round(angular_position, 2):>14} degrees")
            else:
                print(f"{planet.name:<20} | {round(angular_position, 2):>14} grade")
        print("_" * 45)

    def stage_5_ui(self):
        try:
            if self.__repo_planets is None:
                self.set_planet_repo_file()
            if self.__repo_rocket is None:
                self.set_rocket_repo_file()
            if self.__repo_solar_system is None:
                self.set_solar_system_repo_file()

            starting_planet, destination_planet = self.stage_3_5_6_select_planets()

            self.stage_5_ui_printing_data(starting_planet, destination_planet)

        except ui_exception as e:
            print(e)

        except Printer_Ui_Exception as e:
            print(e)

        except ValueError as e:
            print(e)

        except TypeError as e:
            if self.__lang == "1":
                print("Exiting...")
            else:
                print("Iesire...")

    def stage_6_ui(self):
        try:
            if self.__repo_planets is None:
                self.set_planet_repo_file()
            if self.__repo_rocket is None:
                self.set_rocket_repo_file()
            if self.__repo_solar_system is None:
                self.set_solar_system_repo_file()

            starting_planet, destination_planet = self.stage_3_5_6_select_planets()
            self.stage_6_ui_printing_data(starting_planet, destination_planet)

        except ui_exception as e:
            print(e)

        except Printer_Ui_Exception as e:
            print(e)

        except ValueError as e:
            print(e)

        except TypeError as e:
            if self.__lang == "1":
                print("Exiting...")
            else:
                print("Iesire...")

    def stage_6_ui_printing_data(self, starting_planet, destination_planet):
        calc = Calculations()
        print("_" * 150)
        if self.__lang == "1":
            print("Note: We assume that our rocket stops by doing what they did to get going, but in reverse")
            print('      When referring to "the start of the simulation", we consider the 100 years since the planets were all aligned')
        else:
            print("Notă: Presupunem că racheta noastră se oprește făcând ceea ce a făcut pentru a porni, dar în sens invers")
            print('      Când ne referim la „începutul simulării”, luăm în considerare cei 100 de ani de când planetele au fost toate aliniate')

        print(f"{starting_planet.name} ---> {destination_planet.name}")
        planets = self.__repo_solar_system.get_all_planets_extended()
        rocket = self.__repo_rocket.get_rocket()
        days, distance_surfaces, aligned, sp_degrees, dp_degrees = self.__srv.find_the_optimal_window_2(starting_planet, destination_planet, rocket, 100 * 365, planets)
        self.__printer.stage_5_6_printing_data_optimal_window_data(starting_planet, destination_planet, days, aligned, sp_degrees, dp_degrees)
        planet = self.__srv.maximum_escape_velocity(starting_planet, destination_planet)
        time = self.__srv.time_escape_velocity(planet, rocket)
        distance = self.__srv.distance_escape_velocity(0, planet, rocket)
        cruising_distance = distance_surfaces - 2 * distance
        # cruising_velocity -> m/s
        # distance_surfaces -> km, converted to m
        # cruising_time -> s
        cruising_velocity = self.__srv.cruising_velocity(starting_planet, destination_planet)
        cruising_time = calc.convert_kilometres_to_metres(distance_surfaces) / cruising_velocity
        total_cruising_time = cruising_time + time * 2
        self.__printer.stage_3_5_6_ui_printing_data(time, distance, cruising_distance, cruising_time, total_cruising_time)

        if self.__lang == "1":
            print("The angular position of all the planets: ")
        else:
            print("Pozitia unghiulara pentru toate planetele: ")
        self.print_planets_with_angular_position(days + 100 * 365)

        if self.__lang == "1":
            print(f"The beginning of the transfer window is after {days} days since the start of the simulation or {days + 100 * 365} days since all the planets were aligned.")
        else:
            print(f"Începutul ferestrei de transfer este după {days} zile de la începutul simulării sau {days + 100 * 365} zile de când toate planetele au fost aliniate.")
        print("_" * 150)

    def stage_5_ui_printing_data(self, starting_planet: Planet, destination_planet: Planet):
        calc = Calculations()
        rocket = self.__repo_rocket.get_rocket()
        print("_" * 150)
        if self.__lang == "1":
            print("Note: We assume that our rocket stops by doing what they did to get going, but in reverse")
            print('      When referring to "the start of the simulation", we consider the 100 years since the planets were all aligned')
        else:
            print("Notă: Presupunem că racheta noastră se oprește făcând ceea ce a făcut pentru a porni, dar în sens invers")
            print('      Când ne referim la „începutul simulării”, luăm în considerare cei 100 de ani de când planetele au fost toate aliniate')

        print(f"{starting_planet.name} ---> {destination_planet.name}")
        #planet that has the maximum escape velocity
        planet = self.__srv.maximum_escape_velocity(starting_planet, destination_planet)
        planets = self.__repo_solar_system.get_all_planets_extended()

        days, distance_surfaces, aligned, sp_degrees, dp_degrees = self.__srv.find_the_optimal_window_1_optimised(starting_planet, destination_planet, 100 * 365, planets)
        self.__printer.stage_5_6_printing_data_optimal_window_data(starting_planet, destination_planet, days, aligned, sp_degrees, dp_degrees)

        time = self.__srv.time_escape_velocity(planet, rocket)
        distance = self.__srv.distance_escape_velocity(0, planet, rocket)
        cruising_distance = distance_surfaces - 2 * distance
        #cruising_velocity -> m/s
        #distance_surfaces -> km, converted to m
        #cruising_time -> s
        cruising_velocity = self.__srv.cruising_velocity(starting_planet, destination_planet)
        cruising_time = calc.convert_kilometres_to_metres(distance_surfaces) / cruising_velocity
        total_cruising_time = cruising_time + time * 2
        self.__printer.stage_3_5_6_ui_printing_data(time, distance, cruising_distance, cruising_time, total_cruising_time)

        if self.__lang == "1":
            print("The angular position of all the planets: ")
        else:
            print("Pozitia unghiulara pentru toate planetele: ")
        self.print_planets_with_angular_position(days + 100 * 365)

        if self.__lang == "1":
            print(f"The beginning of the transfer window is after {days} days since the start of the simulation or {days + 100 * 365} since all the planets were aligned.")
        else:
            print(f"Începutul ferestrei de transfer este după {days} zile de la începutul simulării sau {days + 100 * 365} de când toate planetele au fost aliniate.")
        print("_" * 150)

    def set_language(self):
        while True:
            self.__printer.print_language_menu()
            language = input(">>> ")
            if language in ["1", "2"]:
                self.__lang = language
                self.__printer = Printer(language)
                return
            else:
                print("Invalid option / Opțiune Invalidă")


    def run(self):
        self.set_language()
        while True:
            self.__printer.print_menu()
            option = input(">>> ")
            match option:
                case "1":
                    self.print_all_planets()

                case "2":
                    self.calculate_escape_velocity_ui()

                case "3":
                    self.calculate_time_distance_escape_velocity_ui()

                case "4":
                    self.stage_3_ui()

                case "5":
                    self.display_the_angular_position_of_each_planet()

                case "6":
                    self.stage_5_ui()

                case "7":
                    self.stage_6_ui()

                case "8":
                    self.change_language()

                case "9":
                    break

                case _:
                    if self.__lang == "1":
                        print("Invalid Option")
                    else:
                        print("Opțiune invalidă")
