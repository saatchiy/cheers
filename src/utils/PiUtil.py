from .pialgorithms.GregoryLeibniz import GregoryLeibniz
# This is a static util class that provides a function for
# calculating the PI number

print("Calculation of PI constant started.")

class PiUtility:

    __DEFAULT_PRECISION = 3
    __precision = ''
    __pi = 0

    @classmethod
    def pi(self, precision):
        if self.__pi == 0:
            if precision:
                self.__precision = precision
            else:
                self.__precision = self.__DEFAULT_PRECISION
                
            self.__calculate_pi()

        return self.__pi

    @classmethod
    def __calculate_pi(self):
        self.__pi = GregoryLeibniz.calculate(self.__precision)
