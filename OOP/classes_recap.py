class Bird:
    def __init__(self, species, colour, can_fly=True):
        self.species = species
        self.colour = colour
        self.wings = 2
        self.can_fly = can_fly
        self.age = 0

    def reproduce(self):
        if self.age < 2:
            return "Too young"
        return "egg"

    def age_up(self, years=1):
        self.age += years

    def get_age(self):
        return self._age


bird = Bird("sparrow", "brown")

bird.age_up(5)
egg = bird.reproduce()
print(egg)


class Penguin(Bird):
    def __init__(self, subspecies, colour=("black", "white")):
        super().__init__("Penguin", colour, False)
        self.subspecies = subspecies

    def hunt_for_fish(self):
        print("splash")


class Rockhopper(Penguin):
    def __init__(self):
        super().__init__("Rockhopper", colour=("yellow, black, white"))


    def collect_rocks(self):
        print("Look at that pile of rocks!")



