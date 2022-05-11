# -What statement about static methods is true
# -R: Static methods serve mostly as utility methods or helper methods, since they cant access or 
# modify a class state
# - Static methods, much like class methods, are methods that are bound to a class rather than its object
# - They do not require a class instance creation. So, they are not dependent on the state of the object

class FixArray():

    contador: int = 1
    def __init__ (self:object):
        FixArray.contador +=1

    @classmethod
    #ligada ao objeto
    def sortr (self: object, arr: str = []):
        return arr.sort()

    @staticmethod
    #Ligada a classe
    def counter (self):
        return self.contador

if __name__ == "__main__":
    arr = FixArray
    arr.sortr([9,3,4,5])
    print(arr.contador())
