class animal():
    def __init__(self):
        self.num_eyes =2
    def breathe(self):
        print("inhale,exhale") 

class fish(animal):
    def __init__(self):
        super.__init__()       
    def swim(self):
        self.breathe()
        print("swim")

a = fish()
print(a.swim())
