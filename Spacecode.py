class Spacecraft:
    def __init__(self, x, y, z, direction):
        self.position = (x, y, z)
        self.direction = direction

    def move_forward(self):
        x, y, z = self.position
        if self.direction == "N":
            self.position = (x, y + 1, z)
        elif self.direction == "S":
            self.position = (x, y - 1, z)
        elif self.direction == "E":
            self.position = (x + 1, y, z)
        elif self.direction == "W":
            self.position = (x - 1, y, z)
        elif self.direction == "Up":
            self.position = (x, y, z + 1)
        elif self.direction == "Down":
            self.position = (x, y, z - 1)

    def move_backward(self):
       
        x, y, z = self.position
        if self.direction == "N":
            self.position = (x, y - 1, z)
        elif self.direction == "S":
            self.position = (x, y + 1, z)
        elif self.direction == "E":
            self.position = (x - 1, y, z)
        elif self.direction == "W":
            self.position = (x + 1, y, z)
        elif self.direction == "Up":
            self.position = (x, y, z - 1)
        elif self.direction == "Down":
            self.position = (x, y, z + 1)

    def turn_left(self):
        if self.direction == "N":
            self.direction = "W"
        elif self.direction == "S":
            self.direction = "E"
        elif self.direction == "E":
            self.direction = "N"
        elif self.direction == "W":
            self.direction = "S"

    def turn_right(self):
        if self.direction == "N":
            self.direction = "E"
        elif self.direction == "S":
            self.direction = "W"
        elif self.direction == "E":
            self.direction = "S"
        elif self.direction == "W":
            self.direction = "N"

    def turn_up(self):
        if self.direction in {"N", "S", "E", "W"}:
            self.direction = "Up"

    def turn_down(self):
        if self.direction in {"N", "S", "E", "W"}:
            self.direction = "Down"


def execute_commands(commands, spacecraft):
    for command in commands:
        if command == "f":
            spacecraft.move_forward()
        elif command == "b":
            spacecraft.move_backward()
        elif command == "l":
            spacecraft.turn_left()
        elif command == "r":
            spacecraft.turn_right()
        elif command == "u":
            spacecraft.turn_up()
        elif command == "d":
            spacecraft.turn_down()


if __name__ == "__main__":
    starting_position = (0, 0, 0)
    starting_direction = "N"
    chandrayaan_3 = Spacecraft(*starting_position, starting_direction)

    commands = ["f", "r", "u", "b", "l"]
    execute_commands(commands, chandrayaan_3)

    print(f"Final Position: {chandrayaan_3.position}")
    print(f"Final Direction: {chandrayaan_3.direction}")
