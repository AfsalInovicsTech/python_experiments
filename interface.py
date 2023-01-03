
import abc

class Exhaust(abc.ABC):

    @abc.abstractmethod
    def sound(self):
        pass


class Akrapovic(Exhaust):

    def sound(self):
        print("Wroom Wroom")


class Yoshimura(Exhaust):

    def sound(self):
        print("Broom Broom")


class NoBrand(Exhaust):
    pass



# a = Exhaust()
# b = Akrapovic()
# b.sound()
# c = Yoshimura()
# c.sound()

d = NoBrand()