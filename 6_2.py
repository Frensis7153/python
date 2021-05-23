class Road:
    def __init__(self, length, width):
        self.__length = length
        self.__width = width

    def mass_of_asphalt(self, mass_of_asphalt_1_cm_thick, number_cm_of_blade_thickness):
        return self.__length * self.__width * mass_of_asphalt_1_cm_thick * number_cm_of_blade_thickness


road = Road(20, 5000)
print(road.mass_of_asphalt(25, 5))
