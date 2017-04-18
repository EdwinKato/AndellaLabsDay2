class Car():
    def __init__(self, name="General", model="GM", type=""):
        self.type = type
        self.model = model
        self.name = name
        self.speed = 0

        if self.name == "Porshe" or self.name == "Koenigsegg":
            self.num_of_doors = 2
        else:
            self.num_of_doors = 4

        if self.type == "trailer":
            self.num_of_wheels = 8
        else:
            self.num_of_wheels = 4

    def is_saloon(self):
        if self.type != "trailer":
            return True
        else:
            return False

    def drive(self, car_speed):
        if self.type == "trailer":
            self.speed = (11 * car_speed)
        else:
            self.speed = 10 ** car_speed
        return self