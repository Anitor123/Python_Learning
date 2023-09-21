import turtle as t
screen = t.Screen()


def move(self):
        self.forward(self.speed)
        self.wall_checker()
        screen.ontimer(self.move)