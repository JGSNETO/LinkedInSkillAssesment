# What is a abstract class ?
# -An abstract classexist only so that other "Concrete" class can inherit from the abstract class
# - You can define a common application for a set of diferent subclasses
class Roar():
    def rugido(self):
        print("Roarrrrr")

class Lion(Roar):
    def speak(self):
        print("Lionnnn")

if __name__ == "__main__":
    
    lion = Lion()
    lion.rugido()
