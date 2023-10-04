class Animal:
    def __init__(self):
        self.num_of_eyes = 2

    def breathe(self):
        print("Inhale and exhale")


class Fish(Animal):
        def __init__(self):
            super().__init__()

        def breathe(self):
            super().breathe()
            print("Doing this underwater")         
    

        def swim(self):
            print("moving in water")


nemo = Fish()
nemo.swim()
nemo.breathe()

print(nemo.num_of_eyes)